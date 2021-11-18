from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from home import views
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('blogpost/', views.blogpost, name='blogpost'),
    path('conditions/', views.conditions, name='conditions'),
    path('signup/', views.signup, name='signup'),
    path('transfersign/', views.transfersign, name='transfersign'),
    path('handlelogin/', views.handlelogin, name='handlelogin'),
    path('transferlogin/', views.transferlogin, name='transferlogin'),
    path('handlelogout/', views.handlelogout, name='handlelogout'),

    path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]
