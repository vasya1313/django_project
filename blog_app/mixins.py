from django.core.exceptions import PermissionDenied


class TitleMixin:
    title = None
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.title:
            context['title'] = self.title

        return context


class StaffRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_staff:
            raise PermissionDenied('Доступ только для сотрудников!')

        return super().dispatch(request, *args, **kwargs)


class AuthorRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user.username:
            raise PermissionDenied("Вы не являетесь автором этого поста!")

        return super().dispatch(request, *args, **kwargs)
