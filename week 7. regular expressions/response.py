from validator_collection import checkers


def main():
    print(email_validation(input("What's your email address?")))


def email_validation(email) -> str:
    return "Valid" if checkers.is_email(email) else "Invalid"


if __name__ == '__main__':
    main()
