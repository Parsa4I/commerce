# Generated by Django 4.0.2 on 2022-02-18 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0017_user_created_listing_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('ELC', 'Electronics'), ('BMM', 'Books, Movies & Music'), ('ART', 'Art'), ('FSH', 'Fashion'), ('THB', 'Toys and Hobbies'), ('SPG', 'Sporting Goods'), ('HBT', 'Health & Beauty'), ('BZI', 'Business & Industrial'), ('HMG', 'Home & Garden'), ('ACS', 'Accessories'), ('JWR', 'Jewerly'), ('OTR', 'Other')], default='OTR', max_length=3),
        ),
    ]