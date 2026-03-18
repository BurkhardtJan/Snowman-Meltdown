from game_logic import *


def main():
    print("Welcome to Snowman Meltdown!")
    while True:
        play_game()
        replay = input("Play again (Default yes, type no to quit): ").lower()
        if replay in ["no", "nein", "n"]:
            break


if __name__ == "__main__":
    main()
