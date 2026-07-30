from typing import Annotated

from ninja import ModelSchema, Schema
from pydantic import EmailStr, StringConstraints, model_validator
from blog_app.models import Post, Category


class PostOutSchema(ModelSchema):
    class Meta:
        model = Post
        fields = ('id', 'title', 'slug', 'content', 'category', 'author', 'publishes', 'created_at')


class PostInSchema(ModelSchema):
    class Meta:
        model = Post
        fields = ( 'title',  'content', 'category', 'publishes')


class PostSearchResultSchema(Schema):
    id: int
    title: str
    slug: str
    headline: str
    rank: float


class CategoryOutSchema(ModelSchema):
    class Meta:
        model = Category
        fields = ('id', 'title', 'slug')


class CategoryInSchema(ModelSchema):
    class Meta:
        model = Category
        fields = ('title',)


class RegisterInSchema(Schema):
    username: Annotated[str, StringConstraints(min_length=3, max_length=20)]
    email: EmailStr
    password: Annotated[str, StringConstraints(min_length=6)]
    password_confirm: Annotated[str, StringConstraints(min_length=6)]


    @model_validator(mode="after")
    def passwords_match(self) -> 'RegisterInSchema':
        if self.password != self.password_confirm:
            raise ValueError("Пароли не совпадают!")
        return self


class RegisterOutSchema(Schema):
    message: str
    username: str
    email: str


class ActivationOutSchema(Schema):
    message: str
    activated: bool


class LoginInSchema(Schema):
    username: Annotated[str, StringConstraints(min_length=3, max_length=20)]
    password: Annotated[str, StringConstraints(min_length=6)]


class LoginOutSchema(Schema):
    success: bool
    message: str
    username: str | None = None
    email: str | None = None
    is_staff: bool | None = None
