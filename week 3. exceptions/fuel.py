def main():
    print(fraction_to_percent())

# convert fraction to decimal
# accepts str in format of 2/3, 4/5 etc
def fraction_to_percent() -> str:
    while True:
        try:
            # makes a list of 3 elements like "2", "/", "4"
            fraction = input("Fraction: ").partition("/")
            # checks for decimal values and that first number is less than second
            if int(fraction[0]) <= int(fraction[2]) and fraction[0].isdecimal() and fraction[2].isdecimal():
                percentage = int(int(fraction[0]) / int(fraction[2]) * 100)
                if percentage == 0:
                    return "E"
                elif percentage == 100:
                    return "F"
                else:
                    return str(percentage) + "%"
        except (ValueError, ZeroDivisionError):
            pass


main()