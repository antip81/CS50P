# https://cs50.harvard.edu/python/2022/psets/4/figlet/

import sys
from pyfiglet import Figlet
import random


def main():
    # TODO: use figlet.getFonts() instead of file to get a list of fonts
    # open the fonts.txt file  in read-only mode
    my_file = open("fonts.txt", "r")
    # split fonts into a list
    data_into_list = my_file.read().split("\n")
    # close the file
    my_file.close()

    # check for arguments in CLI, should be equal to 3 -f or --font and "font" should be in figlet fonts list
    if len(sys.argv) == 3:
        if (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in data_into_list:
            # call print function and pass "font" into it
            figlet_print(sys.argv[2])
        else:
            # exit with error msg
            sys.exit("Invalid usage")
    elif len(sys.argv) == 1:
        # set a random font
        f = random.choice(data_into_list)
        # call print function and pass a "random font" into it
        figlet_print(f)
    else:
        # exit with error msg
        sys.exit("Invalid usage")


def figlet_print(f=str):
    text = input("Input: ")
    f = Figlet(font=f)
    print(f.renderText(text))


if __name__ == '__main__':
    main()
