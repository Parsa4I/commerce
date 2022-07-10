# Generated by Django 4.0.2 on 2022-02-17 18:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0013_item_high_bid_user_user_bid'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='adder',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='item_adder', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='item',
            name='high_bid_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='high_bidder', to=settings.AUTH_USER_MODEL),
        ),
    ]
