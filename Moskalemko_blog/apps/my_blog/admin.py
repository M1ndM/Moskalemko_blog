from django.contrib import admin
from Moskalemko_blog.apps.my_blog.models import Post
from Moskalemko_blog.apps.my_blog.models import Keywords
# Register your models here.
admin.site.register(Post, admin.ModelAdmin)
admin.site.register(Keywords, admin.ModelAdmin)
