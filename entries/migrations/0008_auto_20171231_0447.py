# Generated by Django 2.0 on 2017-12-31 04:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0007_auto_20171231_0251'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='mats_req',
        ),
        migrations.AddField(
            model_name='item',
            name='mats_req',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='entries.Item'),
        ),
    ]
