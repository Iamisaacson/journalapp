from django.contrib import admin
from .models import Post, Author



class PostAdmin(admin.ModelAdmin):
  list_display = ('title', 'author', 'published_date')

admin.site.register(Post, PostAdmin)
admin.site.register(Author)
