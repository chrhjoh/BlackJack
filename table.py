# Should contain the stuff such as cards on tables and wager and so on
class Table:
    
    def __init__(self, players, dealer):
        self.players = players
        self.dealer = dealer

    

    def payout(self):
        for player in self.players:
            if player.status == "Won":
                player.money += 2 * player.wager
    

    def show_open_cards(self):
        for player in self.players:
            print(player.name)
            player.show_hand()
            print()

        print(self.dealer.name)
        print(self.dealer.show_hand())
