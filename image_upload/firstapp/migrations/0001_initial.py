# Generated by Django 2.2 on 2019-12-06 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Summer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagename', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='images/')),
                ('summery', models.CharField(max_length=30)),
            ],
        ),
    ]
