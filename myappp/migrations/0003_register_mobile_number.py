# Generated by Django 3.2.2 on 2021-07-21 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myappp', '0002_register_place'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='mobile_number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
