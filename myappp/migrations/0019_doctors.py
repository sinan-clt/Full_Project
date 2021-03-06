# Generated by Django 3.2.1 on 2021-08-17 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myappp', '0018_rename_name_students_firstname'),
    ]

    operations = [
        migrations.CreateModel(
            name='doctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('mobile', models.BigIntegerField()),
                ('department', models.CharField(max_length=20)),
                ('dob', models.DateField()),
                ('email', models.EmailField(max_length=40)),
            ],
        ),
    ]
