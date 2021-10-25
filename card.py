
class Card:
    
    name_dict = {1 : "Ace", 2 : "Two", 3 : "Three", 4 : "Four", 5 : "Five",
                      6 : "Six", 7 : "Seven", 8 : "Eight", 9 : "Nine", 10 : "Ten",
                      11 : "Jack", 12 : "Queen", 13 : "King"}


    def __init__(self, value, suit):
        if value == 1:
            self.val = 11
        elif  1 < value < 10:
            self.val = value
        else:
            self.val = 10
        self.suit = suit
        self.val_name = self.name_dict[value]

        self.n_value = value # Used for hash

    
    def __repr__(self):
        return f"{self.val_name} of {self.suit}"
    
    def __hash__(self) -> int:
        return self.n_value

    def __eq__(self, other) -> bool:
        return self.n_value == other.n_value and self.suit == other.suit


if __name__ == "__main__":
    print(Card(1, "Spades"))
    print(Card(13, "Club").val, Card(13, "Club").val_name)

