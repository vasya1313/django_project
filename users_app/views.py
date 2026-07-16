from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth.views import LoginView
# from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


from .forms import ProfileForm, CustomLoginForm, CustomUserCreationForm
from users_app.models import Profile


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('blog:index_page')


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'users/profile_detail.html'


    def get_object(self, queryset=None):
         # get_or_create вернёт кортеж (объект, создан_ли)
         # Если профиля ещё нет — он будет создан автоматически
         profile, created = Profile.objects.get_or_create(
             user=self.request.user
         )
         return profile


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'users/profile_update.html'
    success_url = reverse_lazy('users:profile_detail')

    def get_object(self, queryset=None):
        # get_or_create на случай, если пользователь перешел на страницу
        # редактирования раньше, чем просмотра, и профиль еще не создан.
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile


class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'users/login.html'
