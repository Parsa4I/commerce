# Generated by Django 4.0.2 on 2022-02-24 09:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0027_bid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bid',
            name='item',
        ),
        migrations.AlterField(
            model_name='bid',
            name='amount',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='bid',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
