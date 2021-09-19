# Should contain the stuff such as cards on tables and wager and so on
from dealer import Dealer
from deck import Deck
class Table:
    
    def __init__(self, players):
        self.players = players
        self.dealer = Dealer()

    

    def payout(self):
        for player in self.players:
            if player.status == "Won":
                player.money += 2 * player.wager
    

    def show_cards(self):
        for player in self.players:
            print(player.name)
            player.show_hand()
            print()
        print(self.dealer.name)
        print(self.dealer.show_hand())
    
    def new_game(self):
        for player in self.players:
            if player.money <= 0:
                print(f"{player.name} does not have enough money to continue")
                self.players.remove(player)
            else:
                player.status = "Playing"
        self.deck = Deck()
        self.dealer.deal(self.deck, self.players)
        
