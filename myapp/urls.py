from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from django.contrib.auth import views as auth_views
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'myapp'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('building_permit_details/', views.building_permit_details, name='building_permit_details'),
    path('status_details/', views.status_details, name='status_details'),
    path('adminpage/', views.adminpage, name='adminpage'),
    path('adminlogin/', views.adminlogin, name='adminlogin'),
    path('adminsignup/', views.adminsignup, name='adminsignup'),
    path('about/', views.about, name='about'),
    path('privacy/', views.privacy_policy, name='privacy_policy'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('apply/', views.building_permit_application, name='building_permit_application'),
    path('application_details/<int:permit_id>/', views.application_details, name='application_details'),
    path('debug/', views.debug_result_page, name='debug_result_page'),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name ="register/password_reset.html"), name='reset_password'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name = "register/password_reset_sent.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = "register/password_reset_form.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name = "register/password_reset_done.html"), name='password_reset_complete'),
] + staticfiles_urlpatterns()


# staticfiles_urlpatterns()
# static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
