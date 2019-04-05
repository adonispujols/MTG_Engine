import typing


class Player:
    def __init__(self, deck: typing.List):
        self.deck = deck
        self.hand = []
