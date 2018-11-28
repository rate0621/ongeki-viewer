from django.db import models

# Create your models here.

class Music(models.Model):
    """書籍"""
    title       = models.CharField('曲名'    , max_length=255)
    genre       = models.CharField('ジャンル', max_length=255)
    difficult   = models.CharField('難易度'  , max_length=255)
    total_notes = models.IntegerField('総ノーツ数', blank=True, null=True, default=0)
    total_bells = models.IntegerField('総ベル数'  , blank=True, null=True, default=0)
    level       = models.IntegerField('レベル'    , blank=True, null=True, default=0)
    base_rate   = models.IntegerField('譜面定数'  , blank=True, null=True, default=0)

    def __str__(self):
        return self.title

