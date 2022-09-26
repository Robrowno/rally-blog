from django.urls import include, path
from django.contrib import admin
from . import views


# Custom Django Header and Dashboard Title
admin.site.site_header = "RallyBlog Admin Panel"
admin.site.site_title = "RallyBlog Admin Dashboard"

urlpatterns = [
    path('', views.home_page),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('contact', views.contact_page),
    path('follow', views.follow_page),
    path('profile', views.profile_page),
    path('edit-profile', views.edit_profile),
    path('login', views.login_page),
    path('register', views.register_page),
    path('reset-password', views.reset_password_page),


]
