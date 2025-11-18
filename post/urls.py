from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.post_list, name='post_list'),
    path("create/", views.create_post, name='create_post'),
    path("edit/<int:post_id>/", views.edit_post, name='edit_post'),
    path("delete/<int:post_id>/", views.delete_post, name='delete_post'),

    path("register/", views.register, name='register'),
]
