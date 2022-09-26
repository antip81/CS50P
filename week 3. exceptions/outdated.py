# outdated problem set for CS50P
# https://cs50.harvard.edu/python/2022/psets/3/outdated/


def main():
    # call date converter function witch returns a list in format M D YYYYY
    x = date_converter()
    # format output in YYYY-MM-DD where MM and DD shou have lead zeros
    print(f"{int(x[2])}-{int(x[0]):02}-{int(x[1]):02}")


def date_converter() -> list:
    # TODO remove dict and use list.index instead
    months = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12
    }

    while True:
        try:
            date = input("Date: ").strip()

            # check if the first symbol is letter and there is two " " and one ","
            # make sure user inputs date in "Month D, YYYY" format
            if date[0].isalpha() and date.count(" ") == 2 and date.count(",") == 1:
                # splits date into list with 3 elements and removes ","
                date_list = date.replace(",", "").split(" ")
                # check if month is in months dict and day is equal or less 31 and year is equal or less 9999
                if date_list[0] in months and int(date_list[1]) <= 31 and int(date_list[2]) <= 9999:
                    # if so, replaces Month with month equivalent number
                    date_list[0] = months.get(date_list[0])
                    return date_list

            # cheks if the string first symbol in numeric and string has two "/"
            elif date[0].isdecimal() and date.count("/") == 2:
                # splits string into a list
                date_list = date.split("/")
                # cheks if month <=12 day <= 31 and year <= 9999
                if int(date_list[0]) <= 12 and int(date_list[1]) <= 31 and int(date_list[2]) <= 9999:
                    return date_list

        # if user inputs something not corresponding to given formats return to the input part
        except ValueError:
            pass


if __name__ == '__main__':
    main()
