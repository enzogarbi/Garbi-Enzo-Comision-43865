from django.urls import path
from . import views

app_name = 'Blog'

urlpatterns = [
    path('pages/<int:page_id>/', views.page_detail, name='page_detail'),
    path('', views.blog_list, name='blog_list'),
    path('Blog/create/', views.blog_create, name='blog_create'),
    path('create/', views.blog_create, name='blog_create'),
    path('pages/create/', views.page_create, name='page_create'),
    path('blog_edit/<int:blog_id>/', views.blog_edit, name='blog_edit'),
    path('blog_delete/<int:blog_id>/', views.blog_delete, name='blog_delete'),

]
