# Generated by Django 2.0 on 2017-12-25 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0003_auto_20171225_1439'),
    ]

    operations = [
        migrations.AddField(
            model_name='zone',
            name='num_camps',
            field=models.IntegerField(default=1),
        ),
    ]
