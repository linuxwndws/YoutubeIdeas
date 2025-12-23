from django.contrib import admin
from .models import Idea, Vote

class VoteInLine(admin.TabularInline):
    model = Vote


# Register your models here.
@admin.register(Idea)
class IdeaAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title', 'status', 'youtube_url']
    list_filter = ['status']
    inlines = [
        VoteInLine
    ]


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    search_fields = ['reason']
    list_display = ['id', 'idea', 'reason']
    list_filter = ['idea']
