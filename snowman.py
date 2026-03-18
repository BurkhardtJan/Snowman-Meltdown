import random

# Snowman ASCII Art stages
STAGES = [
     # Stage 0: Full snowman
     """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     ( : ) 
     """,
     # Stage 1: Bottom part starts melting
     """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     """,
     # Stage 2: Only the head remains
     """
      ___  
     /___\\ 
     (o o) 
     """,
     # Stage 3: Snowman completely melted
     """
      ___  
     /___\\ 
     """
 ]


# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]



def display_game_state(mistakes, secret_word, guessed_letters):
    """Displays stage of the snowman and revealed secret word"""
    print(STAGES[mistakes])
    revealed_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            revealed_word += letter + " "
        else:
            revealed_word += "_ "   
    print("Word: " + revealed_word)         
            
    
def play_game():
    secret_word = get_random_word()
    print(secret_word) #for testing, remove later
    mistakes = 0
    guessed_letters = []
    print("Welcome to Snowman Meltdown!")
    display_game_state(mistakes, secret_word, guessed_letters)
    guess = input("Guess a letter: ").lower()
    guessed_letters.append(guess)
    
    
if __name__ == "__main__":
    play_game()
