# Should contain the stuff such as cards on tables and wager and so on
from dealer import Dealer
from deck import Deck
from player import Player
class Table:
    
    def __init__(self, players :'list[Player]'):
        self.players = players
        self.dealer = Dealer()

    

    def payout(self):
        for player in self.players:
            if player.status == "Won":
                player.money += 2 * player.wager
    

    def show_money(self):
        print()
        print('######## MONEY AFTER ROUND ########')
        for player in self.players:
            print(player.name)
            print('Total:', player.money)
    
    def new_game(self):
        for player in self.players:
            if player.money <= 0:
                print(f"{player.name} does not have enough money to continue")
                self.players.remove(player)
            else:
                player.hand = set()
                player.status = "Playing"
        self.deck = Deck()
        self.dealer.deal(self.deck, self.players)
        
