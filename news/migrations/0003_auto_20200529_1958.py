# Generated by Django 3.0.6 on 2020-05-29 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment_post',
            new_name='comment_post_id',
        ),
    ]
