from random import choice
import requests

def fetchRandomWord():
    tries = 10
    while tries > 0:
        response = requests.get(f"https://random-word-api.herokuapp.com/word")
        if response.status_code == 200:
            return response.json()[0]  
        else:
            tries -= 1
    return ""

def fetchMeaningofWord(word):
    response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
    if response.status_code == 200:
        return response.json()[0]['meanings'][0]['definitions'][0]['definition']
    else:
        return ""
    
def start_game():
    word = fetchRandomWord()
    meaning = "It's a programming language."
    if word == "":
        word: str = choice(['python', 'java', 'kotlin', 'javascript'])
    else: 
        meaning = fetchMeaningofWord(word)

    print(f'Welcome to the game, Hooman')
    guessed: str = '-' * len(word)
    tries: int = 8
    
    while tries > 0:
        print()
        print("Hooman, you have", tries, "tries")
        if(tries < 5): 
            print()
            print("Here's the hint: ", meaning)
        print()
        
        blanks: int = 0
        print('Word: ', end=' ')
        for char in word:
            if char in guessed:
                print(char, end='')
            else:
                print('-', end='')
                blanks += 1
        print()

        if blanks == 0:
            print('You guessed the word!')
            break

        guess: str = input('Input a letter: ')
        if len(guess) != 1:
            print('Hooman, you call yourself a coder ?' )
            continue

        if guess in guessed:
            print('Hooman, you already guessed it.')
        guessed += guess

        if guess not in word:
            print('No such letter in the word')
            tries -= 1
            if tries == 0:
                print('Hooman, you killed a innocent. Remember it')
                print("\nWord was: ", word)
                break
        

if __name__ == '__main__':
    start_game()