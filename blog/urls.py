from django.urls import path
from .views import index, IndexView
from .views import BlogListView, BlogCreateView, create_done  # 修正

app_name = 'blog'

urlpatterns = [
    path('index', index, name="index"),
    path('index_class', IndexView.as_view(), name="index_class"),
    path('', BlogListView.as_view(), name="blog_list"),
    path('create/', BlogCreateView.as_view(), name='create'),  # 追加
    path('create_done/', create_done, name='create_done'),  # 追加
]
