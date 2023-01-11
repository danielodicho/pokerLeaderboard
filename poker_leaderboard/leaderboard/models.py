from django.db import models

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=100)
    current_amount = models.PositiveIntegerField(default=0)
    peak_amount = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

class Game(models.Model):
    date_time = models.DateTimeField(null=True)
    players = models.ManyToManyField(Player)
    buy_in = models.PositiveIntegerField()
    is_finished = models.BooleanField()
class BuyIn(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
