from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created')
    list_editable = ('status',)
    list_filter = ('status', 'created')
    search_fields = ('title', 'status', 'created') 

admin.site.register(Post, PostAdmin)

