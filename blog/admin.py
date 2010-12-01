from django.contrib import admin
from blog.models import Entry, Category


class EntryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Entry, EntryAdmin)
admin.site.register(Category, CategoryAdmin)
