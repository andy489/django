from django.contrib import admin
from trips.models import Trip, Picture, Paragraph, Destination


class PictureInline(admin.StackedInline):
    model = Paragraph


class ParagraphInline(admin.StackedInline):
    model = Paragraph
    inlines = [
        PictureInline,
    ]


@admin.register(Trip)
class PostAdmin(admin.ModelAdmin):
    list_display = ["created_date", "destination", "from_date", "to_date", "title"]
    inlines = [ParagraphInline]
    ordering = ["created_date"]


# Register your models here.
admin.site.register(Picture)
admin.site.register(Paragraph)
admin.site.register(Destination)
