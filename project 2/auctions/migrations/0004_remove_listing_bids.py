# Generated by Django 4.0.2 on 2022-02-16 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_category_category_name_alter_listing_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='bids',
        ),
    ]
