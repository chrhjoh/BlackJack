import random
from deck import Deck


class Player:

    def __init__(self, name, money = 1000):
        # Init with 2 cards
        self.name = name
        self.hand = []
        self.total = 0
        self.money = money
        self.status = "Playing" # Indicates whether player won
        self.no_aces = 0

    def make_wager(self):
        amount = int(input("Make Wager: "))
        while not 0 < amount < self.money:
            amount = int(input(f"Please enter number between 0 and {self.money}: "))
        self.money -= amount
        self.wager = amount
        return amount
    
    def hit(self, deck):
        card = deck.draw_cards()
        self.hand.append(card)
        if card.val == 11:
            self.no_aces += 1
        self.total += card.val
        
    def stand(self):
        self.status = "Stopped"

    # Print Cards
    def show_hand(self):
        print("Cards on hand: ", self.hand)
    
    def check_score(self):
        while self.total > 21 and self.no_aces > 0:
            self.total -= 10
            self.no_aces -= 1
                
        return self.total

    

if __name__ == "__main__":
    chrib = Player()
    deck = Deck()
    chrib.show_hand()