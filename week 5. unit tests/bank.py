def main():
    user = input("Greeting: ")
    print(value(user))


def value(greeting: str) -> str:
    if "HELLO" in greeting.strip().upper():
        return "$0"

    elif greeting.strip().upper()[0] == 'H':
        return "$20"

    else:
        return "$100"


if __name__ == '__main__':
    main()
