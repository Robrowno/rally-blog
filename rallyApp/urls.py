from django.urls import include, path
from django.contrib import admin
from . import views


# Custom Django Header and Dashboard Title
admin.site.site_header = "RallyBlog Admin Panel"
admin.site.site_title = "RallyBlog Admin Dashboard"

urlpatterns = [
    path('', views.homePage),




]
