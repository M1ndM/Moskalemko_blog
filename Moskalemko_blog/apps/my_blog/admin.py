from django.contrib import admin
from Moskalemko_blog.apps.my_blog.models import Post, Keywords

# Register your models here.
admin.site.register(Post, admin.ModelAdmin)
admin.site.register(Keywords, admin.ModelAdmin)

