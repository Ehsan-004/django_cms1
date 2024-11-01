from django.conf.urls.static import static
from django.urls import path
from django_blog2.settings import MEDIA_URL, MEDIA_ROOT
from .views import IndexView, PostsView, PostDetailView, CategoriesView, CategoryPostsView, TagPostsView

app_name = 'blog'

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('posts/', PostsView.as_view(), name='posts'),
    path('posts/<str:id>', PostDetailView.as_view(), name='post'),
    path('category/<int:cat_id>', CategoryPostsView.as_view(), name='category_posts'),
    path('category/', CategoriesView.as_view(), name='categories'),
    path('tag/<int:tag_id>', TagPostsView.as_view(), name='tag'),
] + static(MEDIA_URL, document_root=MEDIA_ROOT)
