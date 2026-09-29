from django.urls import path
from .views import PostListView, PostDetailView

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('category/<slug:category_slug>/', PostListView.as_view(), name='category_posts'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
]