from django.urls import include, path
from django.contrib import admin
from . import views


# Custom Django Header and Dashboard Title
admin.site.site_header = "RallyBlog Admin Panel"
admin.site.site_title = "RallyBlog Admin Dashboard"

urlpatterns = [
    path('', views.homePage),
    path('contact', views.contactPage),
    path('follow', views.followPage),
    path('login', views.loginPage),
    path('register', views.registerPage),
    path('reset-password', views.resetPasswordPage),


]
