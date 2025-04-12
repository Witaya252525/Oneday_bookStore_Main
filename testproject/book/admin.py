from django.contrib import admin
from .models import Category ,Author ,Book , BookComment

class BookCommentStackInline(admin.StackedInline):
        model = BookComment

class BookTabularInline(admin.TabularInline):
        model = BookComment
        extra = 6

class BookAdmin(admin.ModelAdmin):
        list_display = ['code','name','category','published','show_image']
        list_filter = ['published']
        search_fields = ['code','name']
        prepopulated_fields ={'slug':['name']}

        fieldsets = (
            # Section labeled "Witaya Input" with specified fields
            ('Witaya Input', {'fields': ['code', 'name', 'slug', 'level', 'image', 'description', 'published']}),

            # Section labeled "Category" with specified fields, collapsible in the admin interface
            ('Category', {'fields': ['category', 'author'], 'classes': ['collapse']}),
        )

        # Inline model configuration
        inlines = [BookTabularInline]

admin.site.register (Category)
admin.site.register (Author)
admin.site.register (Book ,BookAdmin)


# Register your models here.
