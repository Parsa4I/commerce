# Generated by Django 4.0.2 on 2022-02-23 18:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0023_item_is_sold_alter_item_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='txt',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='commenter', to=settings.AUTH_USER_MODEL),
        ),
    ]
