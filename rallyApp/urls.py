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
    path('follow', views.followPage),
    path('profile', views.profile_page),
    path('edit-profile', views.edit_profile),
    path('register', views.register,name="register"),
    path('login', views.Login,name="login"),
    path('logout', views.Logout,name="logout"),
    path('forget-password' , views.ForgetPassword , name="forget_password"),
    path('change-password/<token>/' , views.ChangePassword , name="change_password")

]
