# Generated by Django 2.2.7 on 2019-11-23 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rankdemo', '0022_auto_20191123_0334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gameresultview',
            name='base64str',
            field=models.CharField(default='none', max_length=30),
        ),
    ]
