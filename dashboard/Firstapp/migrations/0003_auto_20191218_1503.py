# Generated by Django 2.2 on 2019-12-18 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Firstapp', '0002_auto_20191218_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='civiljobs',
            name='user_civil',
            field=models.ManyToManyField(default=False, to='Userapp.UserReg'),
        ),
        migrations.AlterField(
            model_name='itjobs',
            name='user_it',
            field=models.ManyToManyField(default=False, to='Userapp.UserReg'),
        ),
        migrations.AlterField(
            model_name='mechjobs',
            name='user_mech',
            field=models.ManyToManyField(default=False, to='Userapp.UserReg'),
        ),
    ]
