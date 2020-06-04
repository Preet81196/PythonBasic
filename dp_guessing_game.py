"""
Random Number Guessing Game. By Divyesh Patel - Sun 17 May, 2020
"""
from random import randint as rint


def main():
    random_number = rint(1, 100)
    no_of_guesses = 0
    found = False
    while not found:
        try:
            guessed_number = input("Your Guess: ")
            guessed_number = int(guessed_number)
            no_of_guesses += 1
            if random_number == guessed_number:
                print("Great, Done")
                found = True
            elif guessed_number > random_number:
                print("Guess Lower")
            else:
                print("Guess Higher")

        except ValueError:
            if guessed_number == "exit":
                exit()
            else:
                print("Invalid Input, try again")

    show_results(random_number, no_of_guesses)


def show_results(rn, nog):
    print("\t\t***Results***")
    print("\tYou took", nog, "trails to guess the number", rn)


if __name__ == "__main__":
    main()
