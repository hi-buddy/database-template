# Generated by Django 2.0 on 2017-12-31 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0010_auto_20171231_0520'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='mats_req',
        ),
        migrations.AddField(
            model_name='item',
            name='mats_req',
            field=models.CharField(blank=True, default='', max_length=1024),
        ),
    ]
