# Generated by Django 3.0.1 on 2019-12-21 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commentsapp', '0002_comment_commentforpost'),
        ('postapp', '0001_initial'),
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='UserReg',
        ),
    ]
