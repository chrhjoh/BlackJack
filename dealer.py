# Should have a deal method, and contain rules for the specific dealer

class Dealer:

    def __init__(self, name):
        self.cards = []
        self.name = name
    

    def deal(self, deck, players):
        self.cards.append(deck.draw_cards())
        for player in players:
            player.hand.append(deck.draw_cards())     
            player.open_cards.append(deck.draw_cards())

    def hit(self, deck):
        self.open_cards.append(deck.draw_cards())


    # Print Cards
    def show_hand(self):
        print("Cards on hand: ", self.hand)
