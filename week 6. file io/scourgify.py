import sys
import csv


def main():
    files = get_filenames()
    file_convert(files[0], files[1])


# function to get arguments from user
# also checks if given arguments correspond to the rules
def get_filenames() -> tuple:
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    else:
        if sys.argv[1].count(".") != 1:
            sys.exit("Wrong file extension format")
        if sys.argv[1].split(".")[1] != "csv":
            sys.exit("Not a CSV file")
        else:
            return sys.argv[1], sys.argv[2]


# function to convert csvs
# gets "last, first",house - csv as input
# makes first, last, house - csv as output
def file_convert(input_file, output_file: str):
    try:
        with open(input_file) as csv_in_file:
            reader = csv.DictReader(csv_in_file, delimiter=",")
            with open(output_file, "w", newline="") as csv_out_file:
                fieldnames = ["first", "last", "house"]
                writer = csv.DictWriter(csv_out_file, fieldnames=fieldnames)
                writer.writeheader()
                for row in reader:
                    first: str = row.get("name").split(", ")[1]
                    last: str = row.get("name").split(", ")[0]
                    house: str = row.get("house")
                    writer.writerow({"first": first, "last": last, "house": house})
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == '__main__':
    main()
