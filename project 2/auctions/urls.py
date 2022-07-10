from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('item/<int:item_id>', views.item, name='item'),
    path('create-listing', views.create_listing, name='create_listing'),
    path('add_to_watchlist/<int:item_id>', views.add_to_watchlist, name='add_to_watchlist'),
    path('watchlist', views.watchlist, name='watchlist'),
    path('categories', views.categories, name='categories')
]
