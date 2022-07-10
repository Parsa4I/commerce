from django.contrib import admin
from .models import *


class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'summary', 'category', 'seller',
                    'starting_bid', 'high_bid', 'high_bid_user', 'bid_number')


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'summary', 'item')


class BidAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'item')


# Register your models here.
admin.site.register(Item, ItemAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Bid, BidAdmin)
