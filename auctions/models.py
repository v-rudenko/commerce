from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey, ManyToManyField

# from auctions.views import watchlist


class User(AbstractUser):
    def __str__(self):
        return self.username

class Category(models.Model):
    category_title = models.CharField(max_length=64)
    eng_title = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return f"{self.category_title}"
     
class Lot(models.Model):
    title = models.CharField(max_length=64)
    description  = models.TextField(max_length=512)
    first_bet = models.IntegerField()
    default_bet = models.IntegerField(default=1, blank=True)
    photo = models.URLField(blank=True)
    category = models.ManyToManyField(Category, related_name="lots")
    author = models.ForeignKey(User, default="1", on_delete=CASCADE, related_name="lot")
    is_open = models.BooleanField(default=1)
    winner = models.ForeignKey(User, default=1, on_delete=CASCADE, related_name="winner")
        
    
    def __str__(self):
        return f"Лот №{self.pk} - {self.title}"

class Bet(models.Model):
    lot = models.ForeignKey(Lot, on_delete=CASCADE, blank=True, default=1, related_name="bet")
    bet = models.IntegerField(blank=True)
    client = models.ForeignKey(User, on_delete=CASCADE, blank=True, default=1, related_name="client")
    def __str__(self):
        return f"{self.client}: {self.lot} - {self.bet}"


class Watchlist(models.Model):
    user = models.ForeignKey(User, blank=True, on_delete=CASCADE, related_name="list")
    lot = models.ForeignKey(Lot, blank=True, on_delete=CASCADE, related_name="user")
    def __str__(self):
        return f"{self.id}) {self.user}"

class Comment(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=CASCADE, related_name="author")
    comment = models.CharField(max_length=200, blank=True)
    lot = models.ForeignKey(Lot, on_delete=CASCADE, blank=True, default=1, related_name="comments")
    def __str__(self):
        return f"Лот \"{self.lot.title}\" - {self.user}: {self.comment}"