from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from .models import Category, Product
from ckeditor.fields import RichTextField
from django.utils.safestring import mark_safe


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}

    # def save_model(self, request, obj, form, change):
    #     obj.description = mark_safe(obj.description)
    #     super().save_model(request, obj, form, change)


admin.site.register(Product, ProductAdmin)
