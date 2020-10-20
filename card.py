from enum import Enum, auto

class CardSuit(Enum):
    CLUBS = 0
    DIAMONDS = 1
    HEARTS = 2
    SPADES = 3

class Card:
    def getValue(self):
        return self._value
    def getSuit(self):
        return self._suit
    def __str__(self):
        pass