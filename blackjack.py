# Contains logic for making game run. Could perhaps be split into game loop and a console
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
        print('######## DEALERS DRAW ########')
        table.dealer.show_hand()
        print()

        # Actual game loop
        for player in table.players:
            print(f"######## {player.name.upper()}'S TURN ########")
            player.show_hand()
            player.make_wager()
            player.hit(table.deck)
            player.show_hand()
            player.check_blackjack()
            if player.status == 'Blackjack':
                print('Congratulations you have blackjack')

            while player.status == 'Playing':
                inpt = ask_for_input()

                if inpt == 'h':
                    player.hit(table.deck)
                    if player.total > 21:
                        player.show_hand()
                        print('You are bust sorry')
                        player.status = 'Lost'
                   
                    else:
                        player.show_hand()
                elif inpt == 's':
                    player.stand()


        # After all players make dealers moves
        print("######## DEALERS TURN ########")
        table.dealer.show_hand()
        table.dealer.hit(table.deck)
        table.dealer.check_blackjack()
        table.dealer.show_hand()
        if table.dealer.status == 'Blackjack':
            print('Dealer has blackjack')

        while table.dealer.status == 'Playing':
            table.dealer.hit(table.deck)
            table.dealer.show_hand()
            if table.dealer.total > 21:
                table.dealer.status = 'Lost'
                print('Dealer is bust')
            elif table.dealer.total > 17 and table.dealer.no_aces == 0:
                table.dealer.stand()
        
        print('######## STATUS AFTER ROUND ########')
        for player in table.players:
            if table.dealer.status == 'Blackjack':
                print(player.name, 'Lost!')
            elif player.status == 'Blackjack':
                print(player.name, 'Won!')
            elif table.dealer.status == 'Lost' and player.status == 'Stand':
                player.money += 2 * player.wager
                print(player.name, 'Won!')
            elif table.dealer.status == 'Stand' and player.status == 'Stand' and player.total > table.dealer.total:
                player.money += 2 * player.wager
                print(player.name,  'Won!')
            else:
                print(player.name, 'Lost!')

        table.show_money()
        inpt = input('Do you want to stop enter (q)')

        if inpt == 'q' or len(table.players) == 0:
            playing = False
        else:
            print()
            print('######## NEW GAME ########')
            print()

    
    print('Thanks for playing!')

if __name__ == '__main__':
    main()

