
import random



def choose_word():
    with open('wordlist.txt', 'r') as word_list_file:
        words = word_list_file.readlines()
        return list(random.choice(words).strip().upper())

def display_word(your_word, guessed_letters):
    display = ""
    for letter in your_word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display



def guess_the_word():
    your_word = choose_word()
    guessed_letters = set()
    max_attempts = len(your_word)
    attempts = 0

    print("Welcome to Hangman!")

    while attempts < max_attempts:
        print("\n" + display_word(your_word, guessed_letters))
        user_input = input("Guess a letter: ").upper()

        if user_input in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.add(user_input)

        if user_input not in your_word:
            attempts += 1
            print(f"Wrong guess! You have {max_attempts - attempts} attempts left.")


        if set(your_word) <= guessed_letters:
            print("Congratulations! You guessed the word:", ''.join(your_word))
            break

    if attempts == max_attempts:
        print("Sorry, you ran out of attempts. The word was:", ''.join(your_word))


guess_the_word()