import random

def dice_total():
    return random.randint(1, 6) + random.randint(1, 6)

def main():
    player_1_name = input("Player 1: Enter player 1 name:")
    player_2_name = input("Player 2: Enter player 2 name:")

    player_1_total = dice_total()
    player_2_total = dice_total()

    print(player_1_name + " rolled a total of " + str(player_1_total))
    print(player_2_name + " rolled a total of " + str(player_2_total))

    if player_1_total > player_2_total:
        print(player_1_name + " wins!")
    elif player_1_total < player_2_total:
        print(player_2_name + " wins!")
    else:
        print("It's a tie!")

main()