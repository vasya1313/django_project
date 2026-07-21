from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import AccessMixin


class TitleMixin:
    title = None
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.title:
            context['title'] = self.title

        return context


class StaffRequiredMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if not request.user.is_staff:
            raise PermissionDenied('Доступ только для сотрудников!')
        return super().dispatch(request, *args, **kwargs)


class AuthorRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied("Вы не являетесь автором этого поста!")

        return super().dispatch(request, *args, **kwargs)
