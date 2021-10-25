# Should have a deal method, and contain rules for the specific dealer
from blackjakker import BlackJakker
from player import Player
class Dealer(BlackJakker):

    def deal(self, deck, players :'list[Player]' ):
        self.hit(deck)
        for player in players:
            player.hit(deck)
