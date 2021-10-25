# Super class for behavior of player and dealer
from card import Card
from deck import Deck

class BlackJakker:
    def __init__(self):
        self.hand = set()
        self.total = 0
        self.no_aces = 0
        self.status = 'Playing'
    
    def hit(self, deck : Deck):
        card = deck.draw_cards()
        self.hand.add(card)
        self.calc_score()
    
    def stand(self):
        self.status = "Stand"

    def calc_score(self):
        _sum = 0
        n_aces = 0
        for card in self.hand:
            _sum += card.val
            if card.val == 11:
                n_aces += 1
        while _sum > 21 and n_aces > 0:
            _sum -= 10
            n_aces -= 1
        self.total = _sum

    def check_blackjack(self):
        if self.total == 21 and (Card(11, 'Clubs') in self.hand or Card(11, 'Spades') in self.hand):
            self.status = 'Blackjack'

    def show_hand(self):
        print("Cards on hand:", end=' ')
        print(*self.hand, sep=', ')