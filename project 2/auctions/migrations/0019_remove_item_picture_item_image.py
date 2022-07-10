# Generated by Django 4.0.2 on 2022-02-18 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0018_alter_item_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='picture',
        ),
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.URLField(blank=True, null=True),
        ),
    ]
