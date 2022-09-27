# https://cs50.harvard.edu/python/2022/psets/4/game/
# Prompts the user for a level n . If the user does not input a positive integer, the program should prompt again.
# Randomly generates an integer between 1 and n, inclusive, using the random module.
# Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
#   If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
#   If the guess is larger than that integer, the program should output Too large! and prompt the user again.
#   If the guess is the same as that integer, the program should output Just right! and exit.

def main():
    import random
    # asks for level in function get_number
    lvl: int = get_number("Level :")

    # make an exception for a case when lvl =1 - randrage cannot work with range 1:1
    if lvl != 1:
        prize: int = random.randrange(1, lvl)
    else:
        prize = 1

    guess: int = 0

    while guess != prize:
        guess = get_number("Guess: ")
        if guess > prize:
            print("Too large!")
        elif guess < prize:
            print("Too small!")

    print("Just right!")


# function to get a positive int from user
# accepts prompt as an argument
def get_number(prompt: str) -> int:
    while True:
        try:
            level: str = input(prompt)
            if level.isdecimal() and int(level) > 0:
                return int(level)
            else:
                pass
        except (TypeError, AttributeError):
            pass


if __name__ == '__main__':
    main()
