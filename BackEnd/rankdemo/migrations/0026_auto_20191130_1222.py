# Generated by Django 2.2.5 on 2019-11-30 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rankdemo', '0025_auto_20191127_0912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rank',
            name='username',
            field=models.CharField(max_length=32),
        ),
    ]
