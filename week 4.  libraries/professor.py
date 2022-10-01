# https://cs50.harvard.edu/python/2022/psets/4/professor/

import random


def main():
    lvl = get_level()
    errors: int = 0

    for i in range(1, 11):
        num1: int = generate_integer(lvl)
        num2: int = generate_integer(lvl)
        for j in range(1, 4):
            result: int = int(input(str(num1) + " + " + str(num2) + " = "))
            if result != num1 + num2 and j != 3:
                print("EEE")
            elif result == num1 + num2:
                break
            elif j == 3:
                print(f"{num1} + {num2} = {num1 + num2}")
                errors += 1

    print("Score", 10 - errors)



def get_level() -> int:
    while True:
        try:
            level: int = int(input("Level :"))
            if 0 < level <= 3:
                return level
        except ValueError:
            pass


def generate_integer(level: int) -> int:
    if level == 1:
        return random.randint(1, 9)
    elif level == 2:
        return random.randint(1, 99)
    elif level == 3:
        return random.randint(1, 999)


if __name__ == "__main__":
    main()
