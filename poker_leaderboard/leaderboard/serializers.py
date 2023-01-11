# leaderboard/serializers.py

from rest_framework import serializers
from .models import Player, Game, BuyIn

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['id', 'name', 'current_amount', 'peak_amount']

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'date_time', 'players', 'buy_in', 'is_finished']

class BuyInSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyIn
        fields = ['id', 'player', 'game', 'amount']

