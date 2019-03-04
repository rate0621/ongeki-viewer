from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView
from django.db import connection

from baseratelist.models import Music, MusicDescription

# Create your views here.

def music_list(request):
    """楽曲の一覧"""
    #music_list = Music.objects.exclude(base_rate=None).order_by('base_rate').reverse()
    #music_list = Music.objects.all().order_by('base_rate').reverse()

    query = """
        SELECT
            m.*,
            md.desc
        FROM
            baseratelist_music m
        INNER JOIN
            baseratelist_musicdescription md
        ON
            m.title = md.title
            AND
            m.genre = md.genre
            AND
            m.difficult = md.difficult
        WHERE
            m.base_rate IS NOT NULL
    """
    music_list=exec_query(query);
    return render(request,
                  'baseratelist/music_list.html',     # 使用するテンプレート
                  {'music_list': music_list}          # テンプレートに渡すデータ
            )


def music_edit(request, music_id):
    """楽曲の一覧"""
    music_description = MusicDescription.objects.get_or_create(music_id=music_id, defaults=None)
    return render(request,
                  'baseratelist/music_edit.html',
                  {'music_description': music_description}
            )




def exec_query(sqltext):
    with connection.cursor() as c:
        c.execute(sqltext)
        "Return all rows from a cursor as a dict"
        columns = [col[0] for col in c.description]
        return [
            dict(zip(columns, row))
            for row in c.fetchall()
        ]
