# Should have a deal method, and contain rules for the specific dealer

class Dealer:

    def __init__(self):
        self.cards = []
        self.total = 0
        self.no_aces = 0
    

    def deal(self, deck, players):
        self.hit(deck)
        for player in players:
            player.hit(deck)
            player.hit(deck)

    def hit(self, deck):
        card = deck.draw_cards()
        self.open_cards.append(card)
        if card.val == 11:
            self.no_aces += 1


    # Print Cards
    def show_hand(self):
        print("Cards on hand: ", self.hand)
