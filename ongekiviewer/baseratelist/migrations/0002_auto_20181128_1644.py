# Generated by Django 2.0.1 on 2018-11-28 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseratelist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='base_rate',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='譜面定数'),
        ),
    ]
