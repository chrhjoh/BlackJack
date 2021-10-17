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
            print(player.name+' cards:')
            player.show_hand()
            print('')
        print('Dealer cards:')
        self.dealer.show_hand()

    def show_money(self):
        print()
        print('Amount of money after round')
        for player in self.players:
            print(player.name)
            print('Total:', player.money)
    
    def new_game(self):
        for player in self.players:
            if player.money <= 0:
                print(f"{player.name} does not have enough money to continue")
                self.players.remove(player)
            else:
                player.hand = []
                player.status = "Playing"
        self.deck = Deck()
        self.dealer.deal(self.deck, self.players)
        
