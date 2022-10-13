import sys


def main():
    print(lines_count(get_filename()))


# function to make all checks, returns filename.py
def get_filename() -> str:
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    else:
        if sys.argv[1].count(".") != 1:
            sys.exit("Wrong file extension format")
        if sys.argv[1].split(".")[1] != "py":
            sys.exit("Not a Python file")
        else:
            return sys.argv[1]


# function to count number of lines in a file
def lines_count(file_name) -> int:
    lines: int = 0
    try:
        with open(file_name) as file:
            for line in file:
                #checks if \n or string of spaces or comment exist in a string
                #if not _> +1 line
                if line.startswith("\n") or line.lstrip() == "" or line.lstrip().startswith("#"):
                    pass
                else:
                    lines += 1
    except FileNotFoundError:
        sys.exit("File does not exist")
    return lines


if __name__ == '__main__':
    main()
