from django.shortcuts import render
from django.http import HttpResponse

from baseratelist.models import Music

# Create your views here.

def music_list(request):
    """楽曲の一覧"""
    music_list = Music.objects.all().order_by('base_rate').reverse()
    return render(request,
                  'baseratelist/music_list.html',     # 使用するテンプレート
                  {'music_list': music_list})         # テンプレートに渡すデータ


