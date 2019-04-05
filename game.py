import random
import typing
import player


class Game:
    def __init__(self, players: typing.List["player.Player"], events: typing.List):
        self.players = players
        self.events = events

    def start_game(self):
        for player_ in self.players:
            random.shuffle(player_.deck)
        # TODO send message to find next player
        self.events.append(1)
