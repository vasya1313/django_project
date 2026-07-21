from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from blog_app.models import Category, Post

class PostViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='editor',
            password='password123'
        )
        self.category = Category.objects.create(
            title='Веб-дизайн',
            slug='design'
        )
        self.post = Post.objects.create(
            title='Пост про дизайн',
            slug='design-post',
            content='Текст про дизайн интерфейсов.',
            category=self.category,
            author=self.user,
            publishes=True
        )

    def test_homepage_status_code(self):
        response = self.client.get(reverse('blog:index_page'))
        self.assertEqual(response.status_code, 200)

    def test_homepage_correct_template(self):
        response = self.client.get(reverse('blog:index_page'))
        self.assertTemplateUsed(response, 'blog/index.html')

    def test_homepage_shows_published_posts(self):
        response = self.client.get(reverse('blog:index_page'))
        self.assertContains(response, self.post.title)


    def test_homepage_hides_draft_posts(self):
        Post.objects.create(
            title='Черновик статьи',
            slug='draft-article',
            content='Секретные наброски.',
            category=self.category,
            author=self.user,
            publishes=False
        )
        response = self.client.get(reverse('blog:index_page'))
        self.assertContains(response, 'Пост про дизайн')
        self.assertNotContains(response, 'Черновик статьи')

    def test_post_detail_page_status_code(self):
        response = self.client.get(reverse('blog:post_detail', kwargs={'post_slug': self.post.slug}))
        self.assertEqual(response.status_code, 200)

    def test_post_detail_page_template(self):
        response = self.client.get(reverse('blog:post_detail', kwargs={'post_slug': self.post.slug}))
        self.assertTemplateUsed(response, 'blog/post_detail.html')

    def test_post_detail_page_context(self):
        response = self.client.get(reverse('blog:post_detail', kwargs={'post_slug': self.post.slug}))
        self.assertEqual(response.context['post'], self.post)

    def test_post_detail_returns_404(self):
        response = self.client.get(reverse('blog:post_detail', kwargs={'post_slug': 'non-existent-slug'}))
        self.assertEqual(response.status_code, 404)
