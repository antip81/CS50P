# “Numbers cannot be used in the middle of a plate; they must come at the end. For example,
# AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable.
# The first number used cannot be a ‘0’.”
# - “All vanity plates must start with at least two letters.”
# - “No periods, spaces, or punctuation marks are allowed.”
# - “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    char = ""
    num_in_vanity = False

    #  check for restricted symbols "." " " ","
    if s.count(".") > 0 or s.count(",") > 0 or s.count(" ") > 0:
        return False

    # check for len in between 2 and 6
    if len(s) < 2 or len(s) > 6:
        return False

    # check for first two vanity characters - should be two letters
    if s[0] not in letters or s[1] not in letters:
        return False

    # remaining checks
    for char in s:
        # check if the first number equal to zero
        if char in numbers:
            if int(char) == 0 and not num_in_vanity:
                return False
            # assign Tue to bool = we have number in vanity
            else:
                num_in_vanity = True
        # check if there is no letters after a number
        if char in letters and num_in_vanity:
            return False
    else:
        return True


main()