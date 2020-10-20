import random

class Card:
    def __init__(self, suit, value):
        assert 1 <= suit <= 4 and 1  <= value <= 13
        self._suit = suit
        self._value = value
        self.suitNames = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        self.names = ['Ace','Deuce', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
    
    def getValue(self):
        return self._value
   
    def getSuit(self):
        return self._suit
    def __str__(self):
        return "%s of %s" %(self.names[self.getValue()-1], self.suitNames[self.getSuit()-1])


class CardDeck:
    def __init__(self): 
        self.reset()
    
    def shuffle (self):
        random.shuffle(self._cards)
   
    def getCard(self):  
        return self._cards.pop()
   
    def size(self):
        return len(self._cards)
    
    def reset(self):
        self._cards = []
        for s in range(1, 5):
            for n in range(1, 14):
                self._cards.append(Card(s, n))

deck = CardDeck()
deck.shuffle()

while deck.size()>0:
    card = deck.getCard()
    print("Card {} has value {}".format(card, card.getValue()))