# Generated by Django 3.2.2 on 2021-07-27 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myappp', '0011_userregister_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userregister',
            name='email',
            field=models.EmailField(max_length=60),
        ),
        migrations.AlterField(
            model_name='userregister',
            name='gender',
            field=models.IntegerField(choices=[(0, 'male'), (1, 'female'), (2, 'not specified')]),
        ),
    ]