# Generated by Django 2.0.1 on 2018-12-27 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('difficult', models.CharField(max_length=255, verbose_name='難易度')),
                ('genre', models.CharField(max_length=255, verbose_name='ジャンル')),
                ('title', models.CharField(max_length=255, verbose_name='曲名')),
                ('total_notes', models.IntegerField(blank=True, default=0, null=True, verbose_name='総ノーツ数')),
                ('total_bells', models.IntegerField(blank=True, default=0, null=True, verbose_name='総ベル数')),
                ('base_rate', models.IntegerField(blank=True, default=0, null=True, verbose_name='譜面定数')),
                ('level', models.IntegerField(blank=True, default=0, null=True, verbose_name='レベル')),
            ],
        ),
    ]
