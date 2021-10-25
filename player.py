from card import Card
from blackjakker import BlackJakker

class Player(BlackJakker):

    def __init__(self, name : str, money = 1000):
        BlackJakker.__init__(self)
        # Init with 2 cards
        self.name = name
        self.money = money

    def make_wager(self):
        amount = int(input("Make Wager: "))
        while not 0 < amount < self.money:
            amount = int(input(f"Please enter number between 0 and {self.money}: "))
        self.money -= amount
        self.wager = amount
        return amount
    

if __name__ == "__main__":
    chrib = Player('chrib')
    chrib.show_hand()
    chrib.hand.add(Card(11, 'Clubs'))
    chrib.hand.add(Card(1, 'Clubs'))
    chrib.calc_score()
    chrib.check_blackjack()
    print(chrib.status)
    chrib = Player('test')
    chrib.hand.add(Card(11, 'Hearts'))
    chrib.hand.add(Card(1, 'Hearts'))
    chrib.calc_score()
    chrib.check_blackjack()
    print(chrib.status)