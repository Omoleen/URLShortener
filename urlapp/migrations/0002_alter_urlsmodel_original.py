# Generated by Django 4.1 on 2022-08-17 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urlsmodel',
            name='original',
            field=models.CharField(max_length=1000),
        ),
    ]