# leaderboard/views.py

from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .serializers import PlayerSerializer, GameSerializer, BuyInSerializer
from .models import Player, Game, BuyIn
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.decorators.http import require_http_methods
from rest_framework.permissions import AllowAny
from datetime import datetime
from rest_framework.decorators import action
from rest_framework.response import Response

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    # permission_classes = []
class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    @action(detail=False, methods=['post'], url_name='start_game', url_path="start_game/")
    def start_game(self, request):
        player_ids = request.data.getlist('players')
        players = Player.objects.filter(pk__in=player_ids)
        buy_in_amount = request.data.get('buy-in')
        game = Game(date_time=datetime.now(), buy_in=buy_in_amount, is_finished=False)
        game.save()
        for player in players:
            buy_in = BuyIn(player=player, game=game, amount=buy_in_amount)
            buy_in.save()
        game.players.set(players)
        return render(request, 'end_game.html', {'game': game, 'players': players})

    @action(detail=True, methods=['post'], url_name='end_game', url_path="end_game/")
    def end_game(self, request, pk=None):
        game = self.get_object()
        buy_ins = game.buyin_set.all()
        players = game.players.all()
        total_buy_in = game.buy_in * players.count()
        total_amount = 0
        for buy_in in buy_ins:
            current_amount = int(request.data.get(str(buy_in.player.id)))
            buy_in.amount = current_amount
            buy_in.save()
            total_amount += current_amount
        if total_amount != total_buy_in:
            return Response({'error': 'The sum of current amounts should be equal to the total buy-in amount'},
                            status=400)
        game.is_finished = True
        game.save()
        print("GEEEEEEEEEEEEE")
        return Response({'status': 'Game ended successfully'})



class BuyInViewSet(viewsets.ModelViewSet):
    queryset = BuyIn.objects.all()
    serializer_class = BuyInSerializer
    # permission_classes = []
def leaderboard_view(request):
    players = Player.objects.all()
    return render(request, 'leaderboard.html', {'players': players})


@require_http_methods(["POST"])
def start_game(request):
    player_ids = request.POST.getlist('players')
    players = Player.objects.filter(pk__in=player_ids)
    buy_in_amount = request.POST.get('buy-in')
    game = Game(date_time=datetime.now(), buy_in=buy_in_amount, is_finished=False)
    game.save()
    for player in players:
        buy_in = BuyIn(player=player, game=game, amount=buy_in_amount)
        buy_in.save()
    game.players.set(players)
    return render(request, 'end_game.html', {'game': game})
