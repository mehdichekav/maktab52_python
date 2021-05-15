from random import randint
import argparse
import sys


def game():
    rand_number = randint(0, 100)
    print("\nI have selected a number between 1 to 100...")
    print("You have 5 chances to guess that number...")
    i = 1
    r = 1
    while i < 6:
        user_number = int(input('Enter your number: '))
        if user_number < rand_number:
            print("\nenter higher number")
            print("you now have " + str(5 - i) + " chances left")
            i = i + 1
        elif user_number > rand_number:
            print("\nenter lower number")
            print("you now have " + str(5 - i) + " chances left")
            i = i + 1
        elif user_number == rand_number:
            print("\n!! You have guessed the correct number!")
            r = 0
            break
        else:
            print("This is an invalid number. Please try again")
            print("you now have " + str(5 - i) + " chances left")
            continue
    if r == 1:
        print("Sorry you lost the game!!")
        print("My number was = " + str(rand_number))



print("\nEnd of the Game! Thank you for playing!")

print("The quess is", game())

if __name__ == '__main__':
    print(sys.argv)

    parser = argparse.ArgumentParser(description='Number guessing game')

    parser.add_argument('-f', '--min', help='Minimum value', metavar='int', type=int, default=1)
    parser.add_argument('-t', '--max', help='Maximum value', metavar='int', type=int, default=100)
    parser.add_argument('-g', '--guesses', help='Number of guesses', metavar='int', type=int, default=5)

    args = parser.parse_args(game())

    print(args)

