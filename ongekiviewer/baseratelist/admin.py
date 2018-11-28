from django.contrib import admin
from baseratelist.models import Music

# Register your models here.

#admin.site.register(Music)


class MusicAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'genre', 'difficult', 'total_notes', 'total_bells' , 'level', 'base_rate')  # 一覧に出したい項目
    list_display_links = ('id', 'title')  # 修正リンクでクリックできる項目

admin.site.register(Music, MusicAdmin)




