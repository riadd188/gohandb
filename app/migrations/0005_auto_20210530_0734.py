# Generated by Django 2.2.23 on 2021-05-29 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_item_need'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='memo',
            field=models.TextField(blank=True, verbose_name='備考'),
        ),
    ]