# Should contain the logic that makes the game run
from player import Player
from table import Table

def main():
    print("Welcome to Blackjack")
    print("Try to get as close to 21 as possible. Standard blackjack without splitting")
    print("Dealer will stop at 17")
    playing = True
    names = input("Who is playing, seperated by spaces: ").split()
    
    players = []
    for name in names:
        inpt = int(input(f"{name} How much money do you want: "))
        while inpt < 0:
            inpt = int(input("Please give a positive int: "))
        players.append(Player(name,inpt))

    while playing:
        table = Table(players)
        table.new_game()
        table.show_cards()
        for player in players:
            print(player.name)
            player.make_wager()
        
        # Actual game loop
        for player in table.players:
            print(f"{player.name}'s turn")
            player.show_hand()
            print("What do you want to do: \nh: Hit \ns: Stand \n")
            inpt = input()
            while inpt.lower() != "h" or inpt.lower() != "s":
                raise NotImplementedError
            



    









if __name__ == "__main__":
    main()
 