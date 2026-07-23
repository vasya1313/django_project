from ninja import Router
from ninja.errors import HttpError
from blog_app.models import Post, Category
from ninja_app.schemas import PostOutSchema, PostInSchema, CategoryOutSchema, CategoryInSchema, PostSearchResultSchema
from slugify import slugify
from django.contrib.postgres.search import SearchQuery, SearchVector, SearchRank, SearchHeadline


router = Router()

@router.get('/ping')
def ping(request):
    return {'pong': True}

@router.get('/posts', response=list[PostOutSchema])
async def list_post(request, search: str | None=None, category_id: int | None=None):
    query_set = Post.objects.filter(publishes=True)

    if search:
        query_set = query_set.filter(title__icontains=search)

    if category_id:
        query_set = query_set.filter(category_id=category_id)

    posts = [post async for post in query_set]
    return posts

@router.get('/posts/serch', response=list[PostSearchResultSchema])
async def search_post(request, query: str):
    if not query.strip():
        return []

    vector = (SearchVector("title", weight="A", config="russian") + SearchVector("title", weight="B", config="russian"))
    search_query = SearchQuery(query, config="russian")
    headline = SearchHeadline(
        "content",
        search_query,
        config="russian",
        start_sel="<b>",
        stop_sel="</b>",
        max_words=15,
        min_words=5
    )

    queryset = (
        Post.objects.filter(publishes=True)
        .annotate(
            rank=SearchRank(vector, search_query),
            headline=headline
            )
            .filter(rank__gte=0.01)
            .order_by("-rank")
    )

    results = [
        PostSearchResultSchema(
            id=post.id ,
            title=post.title,
            slug=post.slug,
            headline=post.headline,
            rank=float(post.rank)
        )
        async for post in queryset
    ]
    return results


@router.get('/posts/{post_id}', response=PostOutSchema)
async def get_post(request, post_id: int):
    try:
        post = await Post.objects.aget(pk=post_id)
        return post
    except Post.DoesNotExist:
        raise HttpError(status_code=404, message='Статья не найдена')


@router.post('/posts', response={201: PostOutSchema})
async def create_post(request, payload: PostInSchema):
    post_data = payload.dict()
    post_data['slug'] = slugify(post_data['title'])
    post_data['author'] = request.auth
    post_data['category_id'] = post_data.pop('category')

    new_post = await Post.objects.acreate(**post_data)
    return 201, new_post


@router.get('/categories', response=list[CategoryOutSchema])
async def list_categories(request, search_title: str | None = None):
    query_set = Category.objects.all()
    if search_title:
        query_set = query_set.filter(title__icontains=search_title)
    categories = [category async for category in query_set]
    return categories


@router.get('/categories/{category_id}', response=CategoryOutSchema)
async def get_category(request, category_id: int):
    try:
        category = await Category.objects.aget(pk=category_id)
        return category
    except Category.DoesNotExist:
        raise HttpError(status_code=404, message='Категория не найдена')


@router.post('/categories', response={201: CategoryOutSchema})
async def create_category(request, payload: CategoryInSchema):
    category_data = payload.dict()
    category_data['slug'] = slugify(category_data['title'])
    new_category = await Category.objects.acreate(**category_data)
    return 201, new_category


@router.put('/categories/{category_id}', response=CategoryOutSchema)
async def update_category(request, category_id: int, payload: CategoryInSchema):
    try:
        category = await Category.objects.aget(pk=category_id)
        for attr, value in payload.dict().items():
            setattr(category, attr, value)
        category.slug = slugify(category.title)
        await category.asave()
        return category
    except Category.DoesNotExist:
        raise HttpError(status_code=404, message='Категория не найдена')


@router.delete('/categories/{category_id}', response={204: None})
async def delete_category(request, category_id: int):
    try:
        category = await Category.objects.aget(pk=category_id)
        await category.adelete()
        return 204, None
    except Category.DoesNotExist:
        raise HttpError(status_code=404, message='Категория не найдена')
