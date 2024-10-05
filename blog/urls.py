from django.conf.urls.static import static
from django.urls import path
# from django_blog2 import settings
from django_blog2.settings import MEDIA_URL, MEDIA_ROOT
from .views import IndexView, PostsView, PostDetailView

app_name = 'blog'

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('posts/', PostsView.as_view(), name='posts'),
    path('posts/id=<str:id>', PostDetailView.as_view(), name='post'),
] + static(MEDIA_URL, document_root=MEDIA_ROOT)