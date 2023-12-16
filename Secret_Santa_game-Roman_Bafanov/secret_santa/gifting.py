import random
from .models import Game, Patricipants, Givers
from asgiref.sync import sync_to_async


# @sync_to_async
def get_participants(game):
    # print("Funct started")
    players = []
    for player in Patricipants.objects.select_related('game').filter(game=game):
        print({'id': player.id, 'name': player.name, 'game': player.game.name_of_game})
        players.append(player)
    # print("Funct ended")
    return players

def perform_pairing(games):
    for game in games:
        # начало разибиения на пары
        participants = get_participants(game)

        shift = random.randint(1, len(participants) - 1)
        print("SHIFT: ", shift)
        pairs = {}
        for count, player in enumerate(participants):
            pairs[player] = participants[(count + shift) % len(participants)]
            gifters = Givers(
                game=game,
                givers=player,
                recipient=participants[(count + shift) % len(participants)]
            )
            print(gifters)
            gifters.save()

        # for i in participants:
        #     print(i)
