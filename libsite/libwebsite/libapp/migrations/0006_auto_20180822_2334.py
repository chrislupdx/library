# Generated by Django 2.0 on 2018-08-22 23:34

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('libapp', '0005_auto_20180821_2203'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='borrower',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='liblist',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 22, 23, 34, 58, 712222)),
        ),
    ]
