from django.urls import path
from django.contrib import admin
from . import views


# Custom Django Header and Dashboard Title
admin.site.site_header = "RallyBlog Admin Panel"
admin.site.site_title = "RallyBlog Admin Dashboard"

urlpatterns = [
    path('', views.home_page, name='home'),
    path('post-management/', views.manage_posts, name="manage"),
    path('post-management/add-post/', views.add_post, name="add"),
    path('post-management/edit-post/<int:id>/', views.edit_post, name="edit"),
    path('post-management/delete_post/<int:id>/', views.delete_post, name='delete_post'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('delete/<slug:pk>', views.delete_comment, name='delete_comment'),
    path('update/<slug:pk>', views.update_comment, name='update_comment'),
    path('<slug:slug>/like/', views.like_post, name='like_post'),
    path('contact', views.contact_page, name='contact'),
    path('follow', views.follow_page, name='follow'),
    path('profile', views.profile_page, name="profile"),
    path('edit-profile', views.edit_profile, name='edit_profile'),
    path('delete-profile', views.delete_profile, name='delete_profile'),
    path('register', views.register, name="register"),
    path('login', views.login_func, name="login"),
    path('logout', views.logout_func, name="logout"),
    path('forget-password', views.forget_password, name="forget_password"),
    path('change-password/<token>/', views.change_password, name="change_password"),

]
