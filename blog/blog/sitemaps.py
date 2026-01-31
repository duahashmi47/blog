from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from crashblog.models import Post, Category

class PostSitemap(Sitemap):
    def items(self):
        return Post.objects.filter(status=Post.ACTIVE)

    def lastmod(self, obj):
        return obj.created_at

    def location(self, obj):
        return f'/{obj.category.slug}/{obj.slug}/'

class CategorySitemap(Sitemap):

    def items(self):
        return Category.objects.all()

    def location(self, obj):
        return f'/category/{obj.slug}/'
