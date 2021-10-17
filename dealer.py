# Should have a deal method, and contain rules for the specific dealer

class Dealer:

    def __init__(self):
        self.hand = []
        self.total = 0
        self.no_aces = 0
        self.status = 'Playing'
    

    def deal(self, deck, players):
        self.hit(deck)
        for player in players:
            player.hit(deck)
            player.hit(deck)

    def hit(self, deck):
        card = deck.draw_cards()
        self.hand.append(card)
        if card.val == 11:
            self.no_aces += 1
        self.total += card.val
    
    def check_score(self):

        while self.total > 21 and self.no_aces > 0:
            self.total -= 10
            self.no_aces -= 1
            
        return self.total


    # Print Cards
    def show_hand(self):
        print("Cards on hand: ", self.hand)
