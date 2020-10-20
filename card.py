# from enum import Enum, auto
# import enum

# class CardSuit(Enum):
#     CLUBS = 1
#     DIAMONDS = 2
#     HEARTS = 3
#     SPADES = 4

# class CardValue(enum):

class Card:
    def __init__(self, suit, value):
        assert 1 <= suit <= 4 and 1  <= value <= 13
        self._suit = suit
        self._value = value
        self.suitNames = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        self.names = ['Ace','Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
    def getValue(self):
        return self._value
    def getSuit(self):
        return self._suit
    def __str__(self):
        card = self.names[self.getValue()]  + ' of ' + self.suitNames[self.getSuit()]
        return str(card)

class CardDeck:
    def __init__(self):
        pass
    def shuffle (self):
        pass
    def getCard(self):
        pass
    def size(self):
        pass
    def reset(self):
        pass

# card = Card(3, 1)
# print(card)