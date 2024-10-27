from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, DetailView, ListView
from blog.models import Post, Tag, Category, SubCategory
from django.utils.text import slugify


class IndexView(View):
    template_name = 'index.html'
    http_method_names = ['get', 'post']
    model = Post

    def get(self, request):
        articles = Post.objects.filter(indexed=True)
        most_viewed = Post.objects.order_by('-view_count')[:5]
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
                "view_count": article.view_count,
                "summary": article.summary,
                "picture": article.post_image.url,
                # "slug": article.slug,
            })

        for article in most_viewed:
            most_viewed_articles.append({
                'id': article.id,
                "title": article.title,
                "create_date": article.create_date,
                "view_count": article.view_count,
                "summary": article.summary,
                "picture": article.post_image.url,
                # "slug": article.slug,
            })

        for article in recent:
            recent_articles.append({
                'id': article.id,
                "title": article.title,
                "create_date": article.create_date,
                "view_count": article.view_count,
                "summary": article.summary,
                "picture": article.post_image.url,
                # "slug": article.slug,
            })

        context = {
            'indexed_articles': indexed_articles,
            'most_viewed_articles': most_viewed_articles,
            'recent_articles': recent_articles,
        }
        return render(request, self.template_name, context=context)


class PostsView(ListView):
    model = Post
    template_name = 'list_template.html'
    context_object_name = 'items'
    # paginate_by = 1

    def get_object(self, queryset=None):
        return self.model.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "همه مقالات"
        context['address'] = "همه مقالات"
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'single.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        pid = int(self.kwargs.get('id'))
        if pid:
            p_object = Post.objects.get(pk=pid)
            p_object.view_count += 1
            p_object.save()
            return p_object

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recent_articles = []

        recent = Post.objects.order_by('-create_date')[:5]
        pid = int(self.kwargs.get('id'))
        p_object = Post.objects.get(pk=pid)
        print(p_object)
        post_tags = p_object.tags.all()
        print(post_tags)
        for article in recent:
            recent_articles.append({
                'id': article.id,
                "title": article.title,
                "create_date": article.create_date,
                "summary": article.summary,
                "picture": article.post_image.url,
            })

        context['recent_articles'] = recent_articles
        context['categories'] = Category.objects.all()[:5]
        context['tags_'] = post_tags
        return context


class CategoriesView(ListView):
    model = Category
    template_name = 'category.html'
    context_object_name = 'items'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "دسته بندی ها"
        return context


class CategoryPostsView(ListView):
    # model = Post
    template_name = 'list_template.html'
    context_object_name = 'items'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['address'] = "مقالات در دسته بندی " + Category.objects.get(pk=int(self.kwargs['cat_id'])).name
        context['title'] = context['address']
        return context

    def get_queryset(self):
        posts = []
        sub_cats = SubCategory.objects.filter(category_id=int(self.kwargs['cat_id']))
        for sub_cat in sub_cats:
            sub_cat_posts = Post.objects.filter(sub_category=sub_cat)
            for post in sub_cat_posts:
                posts.append({
                    'id': post.id,
                    'title': post.title,
                    'view_count': post.view_count,
                    'summary': post.summary,
                    'create_date': post.create_date,
                    'post_image': post.post_image,
                })
        return posts


class TagPostsView(ListView):
    model = Tag
    template_name = 'list_template.html'
    context_object_name = 'items'

    def get_queryset(self):
        return Post.objects.filter(tags=Tag.objects.get(pk=int(self.kwargs['tag_id'])))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['address'] = "مقالات با تگ " + Tag.objects.get(id=int(self.kwargs.get('tag_id'))).name
        context['title'] = context['address']
        return context
