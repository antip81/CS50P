from datetime import datetime, date
import sys
import inflect


def main():
    print(how_old_in_minutes(input("Date of birth: ")))


def how_old_in_minutes(user_input: str) -> str:
    p = inflect.engine()
    # if user input is incorrect -> sys.exit
    # parses user_input onto datetime.date class in %Y-%m-%d format
    try:
        user_date = datetime.strptime(user_input, '%Y-%m-%d').date()
    except ValueError:
        sys.exit("Invalid date")
    # substracts today from user_input and makes minutes from days (* 24hrs * 60min)
    minutes = (date.today() - user_date).days * 60 * 24
    # formats and returns sting where
    # andword='' and .capitalize are task requirements
    # uses inflect to convert minutes to words
    return f"{p.number_to_words(minutes, andword='').capitalize()} minutes"


if __name__ == "__main__":
    main()
