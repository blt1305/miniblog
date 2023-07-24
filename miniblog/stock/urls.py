from django.urls import path, re_path
from .views import *
from . import views

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('add_page/', add_page, name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('<int:post_id>/', show_post, name='post'),
    path('category/<int:cat_id>/', show_category, name='category'),
    path('review/<int:post_id>/', views.AddComment.as_view(), name='add_comment'),
    path('<int:post_id>/add_likes/', views.AddLike.as_view(), name='add_likes'),
    path('<int:post_id>/del_likes/', views.DelLike.as_view(), name='del_likes')
]