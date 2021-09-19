import random
from deck import Deck


class Player:

    def __init__(self, name, money = 1000):
        # Init with 2 cards
        self.name = name
        self.hand = []
        self.open_cards = []
        self.total = 0
        self.money = money
        self.status = "Playing" # Indicates whether player won

    def make_wager(self, amount):
        self.money -= amount
        self.wager = amount
        return amount


    # Print Cards
    def show_hand(self):
        print("Cards on hand: ", self.hand)
    

if __name__ == "__main__":
    chrib = Player()
    deck = Deck()
    chrib.show_hand()