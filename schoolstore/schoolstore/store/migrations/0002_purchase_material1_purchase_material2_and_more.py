# Generated by Django 4.1 on 2022-10-14 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='material1',
            field=models.CharField(default='0000000', max_length=250),
        ),
        migrations.AddField(
            model_name='purchase',
            name='material2',
            field=models.CharField(default='0000000', max_length=250),
        ),
        migrations.AddField(
            model_name='purchase',
            name='material3',
            field=models.CharField(default='0000000', max_length=250),
        ),
        migrations.AddField(
            model_name='purchase',
            name='material4',
            field=models.CharField(default='0000000', max_length=250),
        ),
        migrations.AddField(
            model_name='purchase',
            name='material5',
            field=models.CharField(default='0000000', max_length=250),
        ),
    ]