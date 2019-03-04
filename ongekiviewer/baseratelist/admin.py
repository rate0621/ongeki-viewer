from django.contrib import admin
from baseratelist.models import *

# Register your models here.

#admin.site.register(Music)


class MusicAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'genre', 'difficult', 'total_notes', 'total_bells' , 'level', 'base_rate')  # 一覧に出したい項目
    #list_display_links = ('description',)  # 修正リンクでクリックできる項目



class MusicDescriptionAdmin(admin.ModelAdmin):
    class Meta:
        ordering = ['-difficult']

    list_display = ('title', 'genre', 'difficult', 'desc')  # 一覧に出したい項目
    list_display_links = ('title',)  # 修正リンクでクリックできる項目
    

admin.site.register(Music, MusicAdmin)
admin.site.register(MusicDescription, MusicDescriptionAdmin)





