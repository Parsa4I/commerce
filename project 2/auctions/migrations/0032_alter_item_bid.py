# Generated by Django 4.0.2 on 2022-02-25 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0031_alter_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='bid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bids', to='auctions.bid'),
        ),
    ]
