# Generated by Django 3.2.2 on 2021-07-21 20:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myappp', '0006_registersecondtable'),
    ]

    operations = [
        migrations.AddField(
            model_name='registersecondtable',
            name='user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myappp.register'),
            preserve_default=False,
        ),
    ]