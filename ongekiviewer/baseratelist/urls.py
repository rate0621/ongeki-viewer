from django.urls import path
from baseratelist import views

app_name = 'baseratelist'
urlpatterns = [
    # 楽曲
    path('music/', views.music_list,      name='music_list'),   # 一覧
#    path('music/edit/<int:music_id>', views.music_edit,      name='music_edit'),   # 更新
]

