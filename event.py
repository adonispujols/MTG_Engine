class Event:
    NAME = None


class ChooseStartingPlayer(Event):
    NAME = "ChooseStartingPlayer"

    def __init__(self, player_choosing_index):
        self.player_choosing_index = player_choosing_index
