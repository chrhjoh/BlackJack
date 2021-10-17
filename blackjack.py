# Should contain the logic that makes the game run
from player import Player
from table import Table

def ask_for_input():
    inpt = input("What do you want to do: \nh: Hit \ns: Stand \n")
    while (inpt.lower() != "h") and (inpt.lower() != "s"):
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
                inpt = ask_for_input()

                if inpt == 'h':
                    player.hit(table.deck)
                    score = player.check_score()
                    if score > 21:
                        player.show_hand()
                        print('You are bust sorry')
                        player.status = 'Lost'
                    else:
                        player.show_hand()
                elif inpt == 's':
                    player.status = 'Stand'


        # After all players make dealers moves
        print("Dealer's turn:")
        table.dealer.show_hand()
        while table.dealer.status == 'Playing':
            table.dealer.hit(table.deck)
            table.dealer.show_hand()
            score = table.dealer.check_score()
            if score > 21:
                table.dealer.status = 'Lost'
                print('Dealer is bust')
            elif score > 17 and table.dealer.no_aces == 0:
                table.dealer.status = 'Stand'
        
        for player in table.players:
            if table.dealer.status == 'Lost' and player.status == 'Stand':
                player.money += 2 * player.wager
                print(player.name, 'Won!')
            elif table.dealer.status == 'Stand' and player.status == 'Stand' and player.total > table.dealer.total:
                player.money += 2 * player.wager
                print(player.name,  'Won!')
            else:
                print(player.name, 'Lost!')

        table.show_money()
        inpt = input('Do you want to stop enter (q)')

        if inpt == 'q':
            playing = False

    
    print('Thanks for playing!')

if __name__ == '__main__':
    main()

