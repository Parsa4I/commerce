from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver

class User(AbstractUser):
    watchlist_ids = set()

    def __str__(self):
        return self.username


class Item(models.Model):
    CATEGORY_CHOICES = [
        ('ELC', 'Electronics'),
        ('BMM', 'Books, Movies & Music'),
        ('ART', 'Art'),
        ('FSH', 'Fashion'),
        ('THB', 'Toys and Hobbies'),
        ('SPG', 'Sporting Goods'),
        ('HBT', 'Health & Beauty'),
        ('BZI', 'Business & Industrial'),
        ('HMG', 'Home & Garden'),
        ('ACS', 'Accessories'),
        ('JWR', 'Jewerly'),
        ('OTR', 'Other')
    ]

    title = models.CharField(max_length=50)
    summary = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    image = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=3, choices=CATEGORY_CHOICES, default='OTR')
    seller = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='item_seller')
    starting_bid = models.IntegerField()
    high_bid = models.IntegerField(null=True, blank=True)
    high_bid_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='high_bidder')
    bid_number = models.IntegerField(default=0)
    is_sold = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}: {self.summary}'


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commenters', null=True)
    comment_text = models.CharField(max_length=1000, null=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='commented_items', null=True)
    summary = models.CharField(max_length=33, null=True)

    def save(self, *args, **kwargs):
        self.summary = (self.comment_text)[:30] + '...'
        super().save(*args, **kwargs)


class Bid(models.Model):
    amount = models.IntegerField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)


class Watchlist_Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)


@receiver(pre_delete, sender=Bid)
def delete_bid(sender, instance, using, **kwargs):
    item = instance.item
    item.bid_number -= 1
    bids = Bid.objects.filter(item=item)
    try:
        high_bid = bids.order_by('-amount')[1]
        item.high_bid = high_bid.amount
        item.high_bid_user = high_bid.user
    except:
        item.high_bid = None
        item.high_bid_user = None
    item.save()
