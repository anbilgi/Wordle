# This is a sample Python script.
from wordle import Wordle

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    wordle = Wordle("APPLE")
    print(wordle)

    while wordle.is_attempt_allowed:
        x = input("Enter your guess:")
        wordle.attempt(x)
        result = wordle.guess(x)
        print(*result, sep="\n")

        if wordle.is_solved:
            print("You have guessed it right!")
            break

    if not wordle.is_solved:
        print("uhho! Better luck next time..")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
