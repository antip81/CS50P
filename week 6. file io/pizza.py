from tabulate import tabulate
import csv
import sys


def main():
    list_of_values = csv_to_list(get_filename())
    print(tabulate(list_of_values, headers="firstrow", tablefmt="grid"))


def get_filename() -> str:
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    else:
        if sys.argv[1].count(".") != 1:
            sys.exit("Wrong file extension format")
        if sys.argv[1].split(".")[1] != "csv":
            sys.exit("Not a CSV file")
        else:
            return sys.argv[1]


# function to convert a CSV to a list
def csv_to_list(filename: str) -> list:
    table = []
    try:
        with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            for row in csv_reader:
                table.append(row)
    except FileNotFoundError:
        sys.exit("File does not exist")
    return table


if __name__ == '__main__':
    main()
