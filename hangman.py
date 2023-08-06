from random import choice

def start_game():
    word: str = choice(['python', 'java', 'kotlin', 'javascript'])

    print(f'Welcome to the game, Hooman')

    guessed: str = '-' * len(word)
    tries: int = 8
    
    while tries > 0:
        print()
        print("Hoomna, you have", tries, "tries")
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
                break
        

if __name__ == '__main__':
    start_game()