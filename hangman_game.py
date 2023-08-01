import random

from words import word_list


def getword():
    word = random.choice(word_list)
    return word.upper()


def play(word):
    word_completion = "_" * len(word)
    tries = 6
    guessed_words = []
    guessed_letters = []
    gussed = False
    print("Lets play Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")

    while not gussed and tries > 0:
        guess = input("Enter letter or word to guess").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("you have already guessed this letter", guess)
            elif guess not in word:
                print(guess, "not in word")
                tries -= 1
                print(display_hangman(tries))
                print(word_completion)
                print("\n")
                guessed_letters.append(guess)
            else:
                print("Good job", guess, "is in the word")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                print(word_completion)
                if "_" not in word_completion:
                    gussed = True

        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You have already guessed the word", guess)
            elif guess != word:
                print(guess, "not in the word")
                guessed_words.append(guess)
                tries -= 1
                print(display_hangman(tries))
                print(word_completion)
                print("\n")
            else:
                gussed = True
                word_completion = word

        else:
            print("Not a valid guess")
            print(display_hangman(tries))
            print(word_completion)
            print("\n")

    if gussed:
        print("Congrats you guessed te word " + word)
    else:
        print("Sorry you ran out if chances the word is " + word + " may be next time")


def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        # head, torso, both arms, and one leg
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,
        # head, torso, and both arms
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        """,
        # head, torso, and one arm
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        """,
        # head and torso
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        # head
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        """,
        # initial empty state
        """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """
    ]
    return stages[tries]


def main():
    word = getword()
    play(word)

    while input("PLay again Y or N ").upper() == 'Y':
        word = getword()
        play(word)


if __name__ == "__main__":
    main()
