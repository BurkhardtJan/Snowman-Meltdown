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
    if mistakes == 3:
        print("Game Over! The word was: " + secret_word)
        return False
   
    else:
        for letter in secret_word:
            if letter not in guessed_letters:
                return True 
        print("Congratulations, you saved the snowman!")
        return False    
    
    
def play_game():
    secret_word = get_random_word()
    mistakes = 0
    game_running = True
    guessed_letters = []
    print("Welcome to Snowman Meltdown!")
    display_game_state(mistakes, secret_word, guessed_letters)
    while game_running:
        guess = input("Guess a letter: ").lower()
        guessed_letters.append(guess)
        if guess not in secret_word:
            mistakes+=1
        display_game_state(mistakes, secret_word, guessed_letters)
        game_running  = check_game_over(mistakes, secret_word, guessed_letters)
    
    
if __name__ == "__main__":
    play_game()
