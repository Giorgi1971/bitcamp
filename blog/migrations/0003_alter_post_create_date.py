# Generated by Django 4.0.1 on 2022-01-18 21:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_category_cat_image_post_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 18, 21, 4, 19, 667644, tzinfo=utc)),
        ),
    ]
