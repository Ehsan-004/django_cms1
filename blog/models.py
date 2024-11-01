from django.db import models
from django.utils.timezone import now
from django_quill.fields import QuillField


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default='توضیح خلاصه دسته بندی')
    image = models.ImageField(upload_to='categories', default='categories/default.jpg')

    class Meta:
        verbose_name_plural = 'Categories'
        verbose_name = 'Category'
        db_table = 'categories'

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default='توضیح خلاصه زیر دسته بندی')
    image = models.ImageField(upload_to='subcategories', default='subcategories/default.jpg')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Sub-categories'
        verbose_name = 'Sub-category'
        db_table = 'sub_categories'

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Tags'
        verbose_name = 'Tag'
        db_table = 'tags'

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    post_image = models.ImageField(upload_to="post_images", default='default.jpg')
    content = QuillField()
    summary = models.TextField(max_length=500, default="خلاصه پست")
    create_date = models.DateTimeField(default=now)
    view_count = models.IntegerField(default=0)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')
    indexed = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Posts'
        verbose_name = 'Post'
        db_table = 'posts'

    def __str__(self):
        return self.title

