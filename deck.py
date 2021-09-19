import random
from card import Card

class Deck:
    
    def __init__(self):
        self.cards = []
        self.make_deck()
        self.shuffle()
        

    # Initialize full deck (all 52 cards)
    def make_deck(self):
        self.suits = ["Clubs", "Spades", "Hearts", "Diamonds"]
        self.values = [i for i in range(1, 14)]

        self.cards = [Card(val, suit) for val in self.values for suit in self.suits]
    
    def shuffle(self):
        random.shuffle(self.cards)


    # Draw card and remove it
    def draw_cards(self, amount):
        return [self.cards.pop(0) for _ in range(amount)]





if __name__ == "__main__":
    deck = Deck()
    print(deck.cards)
    deck.shuffle()
    print(deck.cards)
    print(deck.draw_cards(3))