from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, DetailView, ListView
from blog.models import Post, Tag, Category, SubCategory


class IndexView(View):
    template_name = 'index.html'
    http_method_names = ['get', 'post']
    model = Post
    def get(self, request):
        articles = Post.objects.filter(indexed=True)
        most_viewed = Post.objects.order_by('view_count')[:5]
        recent = Post.objects.order_by('-create_date')[:5]

        indexed_articles = []
        most_viewed_articles = []
        recent_articles = []

        for article in articles:
            indexed_articles.append({
                'id': article.id,
                "title": article.title,
                "create_date": article.create_date,
                # "comment_count": Comment.objects.filter(article=article).count(),
                "summary": article.summary,
                "picture": article.post_image.url,
            })

        for article in most_viewed:
            most_viewed_articles.append({
                'id': article.id,
                "title": article.title,
                "create_date": article.create_date,
                "summary": article.summary,
                "picture": article.post_image.url,
            })

        for article in recent:
            recent_articles.append({
                'id': article.id,
                "title": article.title,
                "create_date": article.create_date,
                "summary": article.summary,
                "picture": article.post_image.url,
            })

        context = {
            'indexed_articles': indexed_articles,
            'most_viewed_articles': most_viewed_articles,
            'recent_articles': recent_articles,
        }
        return render(request, self.template_name, context=context)



class PostsView(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 1

    def get_object(self, queryset=None):
        return self.model.objects.all()


class PostDetailView(DetailView):
    model = Post
    template_name = 'single.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        pid = int(self.kwargs.get('id'))
        if pid:
            p_object = Post.objects.get(pk=pid)
            return p_object

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recent_articles = []

        recent = Post.objects.order_by('-create_date')[:5]

        for article in recent:
            recent_articles.append({
                "title": article.title,
                "create_date": article.create_date,
                "summary": article.summary,
                "picture": article.post_image.url,
            })
        context['recent_articles'] = recent_articles
        context['categories'] = Category.objects.all()[:5]
        return context
