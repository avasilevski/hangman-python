import random

# variable to record the running state of the game
is_running = True
# variable to keep count of the tries
tries = 3

# list of words avaliable for playing
word_list = ["ardvark", "baboon", "camel"]

# variable to hold the hidden word displayed to the player
display = []
# get random word from the list
word = word_list[random.randint(0, len(word_list) - 1)]
def generate_display(word):
    '''
    Generate a hidden word to display to the player
    Args:
        word (string): the full word
    Returns:
        dispay (list): the hidden word to display
    '''
    # Check if 'word' is a string and not empty
    if not isinstance(word, str) or not word:
        raise ValueError("The 'word' parameter must be a non-empty string.")
    global display
    for char in word:
        display += "_"
    return display

def check_empty(word, display, guess):
    '''
    Check the empty spaces in the variable display and update it with a char if it is correct
    Args:
        word (string): the full word
        display (list): the hidden word which the player is working on
        guess (string): guessed character
    '''
    global is_running
    match = False
    global tries
    for i in range(len(word)):
        if(guess == word[i]):
            display[i] = guess
            match = True      
    if(not match):
        tries -= 1

def game_over_contitions(display, word):
    '''
    Checks the game condidion if the player won or lost the game
    Args:
        display(list): the hidden word which the player was working on to solve
        word(string): full answer which the player was working towards
    '''
    if("".join(display) == word):
        print(f"You won! the right word was: {word}")
    else:
        print(f"Your answers didn't match, the right word was: {word}")

# initial empty display
display = generate_display(word)

# game starts here
while(is_running):
    if(tries <= 0):
        is_running = False
        break
    print(f"Word to guess: {display}")
    print("Guess a letter?")
    guess = input().lower()
    check_empty(word, display, guess)

    # Check for the victory condition
    if "_" not in display:
        is_running = False
        break

    print(f"{tries} more tries available!")


# game over! check if you finish the game successfuly or not
game_over_contitions(display, word)