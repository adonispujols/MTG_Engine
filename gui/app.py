import collections

import game
import player
import event
from gui import custom_event_handler


class Application:
    def __init__(self):
        self.events = collections.deque()
        self.game = self.init_game()

    def init_game(self):
        deck_0 = []
        deck_1 = []
        for i in range(20):
            deck_0.append("0: " + str(i))
            deck_1.append("1: " + str(i))
        return game.Game([player.Player(deck_0), player.Player(deck_1)],
                         custom_event_handler.EventHandler(self.events))

    def run(self):
        self.game.start()
        self.main_loop()

    def main_loop(self):
        while True:
            # TODO need to add sleep
            if self.events:
                dequeued_event: "event.Event" = self.events.popleft()
                if dequeued_event.NAME == event.ChooseStartingPlayer.NAME:
                    print("did the thing")
                    # noinspection PyTypeChecker
                    # TODO implement states
                    # choose_starting_player(dequeued_signal)
