# Generated by Django 4.0.2 on 2022-02-17 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_product_summary_alter_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='picture',
            field=models.ImageField(default='./static/auctions/img/no_image.png', upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='summary',
            field=models.CharField(max_length=50),
        ),
    ]
