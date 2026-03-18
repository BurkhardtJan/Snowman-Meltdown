import random
from ascii_art import STAGES


# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """Displays stage of the snowman and revealed parts of secret word"""
    print(STAGES[mistakes])
    revealed_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            revealed_word += letter + " "
        else:
            revealed_word += "_ "   
    print("Word: " + revealed_word)  
    print("\n")       


def check_game_over(mistakes, secret_word, guessed_letters):
    """Checks if game is is over. If yes, displays final message."""
    if mistakes == len(STAGES) - 1:
        print("Game Over! The word was: " + secret_word)
        return False
   
    else:
        for letter in secret_word:
            if letter not in guessed_letters:
                return True 
        print("Congratulations, you saved the snowman!")
        print(STAGES[mistakes].replace("o", "^"))
        return False    
    
def guess_input(guessed_letters):
    """Handels and checks the input of the guessed letter"""
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess)!=1 or not guess.isalpha():
            print("Invalid input! Please enter a single letter")
        elif guess in guessed_letters:
            print("You already guessed " + guess +". Do you want the snowman to melt?")
            break
        else:
            break    
    return guess
    
        
def play_game():
    """Single round of the game"""
    secret_word = get_random_word()
    mistakes = 0
    game_running = True
    guessed_letters = []    
    display_game_state(mistakes, secret_word, guessed_letters)
    while game_running:
        guess = guess_input(guessed_letters)
        guessed_letters.append(guess)
        if guess not in secret_word:
            mistakes+=1
        display_game_state(mistakes, secret_word, guessed_letters)
        game_running  = check_game_over(mistakes, secret_word, guessed_letters)
 
    
def main():
    print("Welcome to Snowman Meltdown!") 
    while True:
        play_game()   
        replay = input("Play again (yes/no): ").lower()
        if replay in ["no", "nein", "n"]:
            break
    
if __name__ == "__main__":
    main()
