from django.shortcuts import render
from django.views import View
from blog.models import Post, Tag, Category


class IndexView(View):
    template_name = 'index.html'
    http_method_names = ['get', 'post']
    model = Post
    def get(self, request):
        articles = Post.objects.filter(indexed=True)
        most_viewed = Post.objects.order_by('view_count')[:5]
        recent = Post.objects.order_by('create_date')[:5]

        indexed_articles = []
        most_viewed_articles = []
        recent_articles = []

        for article in articles:
            indexed_articles.append({
                "title": article.title,
                "create_date": article.create_date,
                # "comment_count": Comment.objects.filter(article=article).count(),
                "summary": article.summary,
                "picture": article.post_image.url,
            })

        for article in most_viewed:
            most_viewed_articles.append({
                "title": article.title,
                "create_date": article.create_date,
                "summary": article.summary,
                "picture": article.post_image.url,
            })

        for article in recent:
            recent_articles.append({
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
