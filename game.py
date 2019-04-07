import random
import typing

import event
import event_handler
import player


class Game:
    def __init__(self, players: typing.List["player.Player"],
                 core_event_handler: "event_handler.EventHandler"):
        self.players = players
        self.core_event_handler = core_event_handler

    def start(self):
        for player_ in self.players:
            random.shuffle(player_.deck)
        self.core_event_handler.emit_event(event.ChooseStartingPlayer)

    def finish_starting(self, starting_player):
        print("starting plyaer: " + starting_player);
