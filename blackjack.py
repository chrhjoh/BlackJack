# Should contain the logic that makes the game run
from player import Player
from table import Table

def ask_for_input():
    inpt = input("What do you want to do: \nh: Hit \ns: Stand \n")
    while inpt.lower() != "h" or inpt.lower() != "s":
        inpt = input("Not accepted input, please give input: \nh: Hit \ns: Stand \n")
    
    return inpt

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
        
        # Actual game loop
        for player in table.players:
            print(f"{player.name}'s turn")
            player.show_hand()
            player.make_wager()
            score = player.check_score()

            while player.status == 'Playing':
            

                if inpt == 'h':
                    player.hit()
                    score = player.check_score()

                    if score > 21:
                        print('You are bust sorry')
                        player.status = 'Lost'
                    elif
                
            



    









if __name__ == "__main__":
    main()
 