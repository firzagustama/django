# Generated by Django 2.2.7 on 2019-11-11 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20191111_2029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detail',
            name='portofolio',
        ),
        migrations.AlterField(
            model_name='detail',
            name='experience',
            field=models.IntegerField(),
        ),
    ]