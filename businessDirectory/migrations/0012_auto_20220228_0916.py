# Generated by Django 3.1.5 on 2022-02-28 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('businessDirectory', '0011_auto_20220228_0915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='address',
            field=models.CharField(max_length=100),
        ),
    ]