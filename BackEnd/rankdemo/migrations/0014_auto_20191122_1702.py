# Generated by Django 2.2.7 on 2019-11-22 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rankdemo', '0013_rank_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rank',
            name='level',
            field=models.CharField(default='Not clear yet', max_length=16),
        ),
    ]