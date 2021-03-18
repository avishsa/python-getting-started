# Generated by Django 3.1.7 on 2021-03-18 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forecast', '0002_auto_20210317_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forecast',
            name='lat',
            field=models.FloatField(verbose_name='lat'),
        ),
        migrations.AlterField(
            model_name='forecast',
            name='lon',
            field=models.FloatField(verbose_name='lon'),
        ),
        migrations.AlterField(
            model_name='forecast',
            name='precipitation',
            field=models.FloatField(verbose_name='precipitation'),
        ),
        migrations.AlterField(
            model_name='forecast',
            name='temperature',
            field=models.FloatField(verbose_name='temperature'),
        ),
    ]
