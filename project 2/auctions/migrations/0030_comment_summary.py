# Generated by Django 4.0.2 on 2022-02-24 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0029_item_bid'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='summary',
            field=models.CharField(max_length=33, null=True),
        ),
    ]
