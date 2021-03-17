# Generated by Django 3.1.7 on 2021-03-17 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forecast', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forecast',
            name='forecast_time',
            field=models.DateTimeField(verbose_name='forecast time'),
        ),
        migrations.AlterField(
            model_name='forecast',
            name='lat',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='lat'),
        ),
        migrations.AlterField(
            model_name='forecast',
            name='lon',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='lon'),
        ),
        migrations.AlterField(
            model_name='forecast',
            name='precipitation',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='precipitation'),
        ),
        migrations.AlterField(
            model_name='forecast',
            name='temperature',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='temperature'),
        ),
    ]
