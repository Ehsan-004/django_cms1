from django.contrib import admin
from .models import Post, Tag, Category, SubCategory


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'create_date', 'sub_category')


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', )


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )


admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)

