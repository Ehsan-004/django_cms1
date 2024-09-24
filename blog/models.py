from django.db import models
from django.utils.timezone import now
from django_quill.fields import QuillField
from user.models import Profile

class Category(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = 'Categories'
        verbose_name = 'Category'

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = QuillField()
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    create_date = models.DateTimeField(default=now)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title