class States:
    def __init__(self, game):
        self.game = game
        self.choosing_starting_player = ChoosingStartingPlayer(game)


class ChoosingStartingPlayer:
    def __init__(self, game):
        self.game = game


