from django.urls import path
from . import views as app_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('authentication/login/',auth_views.LoginView.as_view(template_name = 'Authentications/login.html'),name='login'),
    path('authentication/register/',app_views.RegisterView.as_view(template_name = 'Authentications/register.html'),name='register'),
    path('authentication/logout/',auth_views.LogoutView.as_view(template_name = 'Authentications/logout.html'),name='logout'),
    path('authentication/password-reset/',auth_views.PasswordResetView.as_view(template_name = 'Authentications/password_reset_form.html'),name='password_reset'),
    path('authentication/password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name = 'Authentications/password_reset_done.html'),name='password_reset_done'),
    path('authentication/password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name = 'Authentications/password_reset_confirm.html'),name='password_reset_confirm'),
    path('authentication/password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name = 'Authentications/password_reset_complete.html'),name='password_reset_complete'),
]

