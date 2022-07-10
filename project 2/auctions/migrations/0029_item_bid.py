# Generated by Django 4.0.2 on 2022-02-24 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0028_remove_bid_item_alter_bid_amount_alter_bid_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='bid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bids', to='auctions.bid'),
        ),
    ]