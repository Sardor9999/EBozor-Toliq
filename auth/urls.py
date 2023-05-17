from django.urls import path
from .views import register_user, logout_user, login_user,user_password_reset
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', register_user, name="register"),
    path('login/', login_user, name = "login_user"),
    path('logout/', logout_user, name = "logout_user"),
    path('password/reset/', user_password_reset, name='password_reset'),
    path('password_reset/done', auth_views.PasswordResetView.as_view(template_name='auth/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetView.as_view(template_name='auth/password_reset_confirm.html'),name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="auth/password_reset_complete.html"), name='password_reset_complete')

]