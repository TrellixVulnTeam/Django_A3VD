# Generated by Django 2.1.7 on 2019-02-15 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_userinfo_tel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='tel',
            field=models.IntegerField(default='13512345678', max_length=11),
        ),
    ]
