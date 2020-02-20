from django.contrib import admin
from Moskalemko_blog.apps.my_blog.models import Post, Keywords, Author

class PostAdmin(admin.ModelAdmin):
    search_fields = ['post_title']
    list_filter = ['id']

# Register your models here.
admin.site.register(Post,PostAdmin)
admin.site.register(Keywords, admin.ModelAdmin)
admin.site.register(Author, admin.ModelAdmin)
