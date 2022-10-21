import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # parse input string
    matches = re.search("^(\d+)[:]?(\d+)? (AM|PM) (to|.) (\d+)[:]?(\d+)? (AM|PM)$", s)

    # if matches exists:
    if matches:
        start_hours: int = matches.group(1)

        # check if minutes are in range of 0 to 59
        # if not - valueerror
        if matches.group(2) and 0 <= int(matches.group(2)) < 60:
            start_minutes: int = int(matches.group(2))
        elif matches.group(2) and (int(matches.group(2)) > 59 or int(matches.group(2)) < 0):
            raise ValueError
        else:
            # if user doesnt give minutes -> minutes = 0
            start_minutes: int = 0

        start_postfix: str = matches.group(3)

        # check if "to" was omitted by a user -> valueerror
        if matches.group(4) != "to":
            raise ValueError

        end_hours: int = matches.group(5)

        if matches.group(6) and 0 <= int(matches.group(6)) < 60:
            end_minutes: int = int(matches.group(6))
        elif matches.group(6) and (int(matches.group(6)) > 59 or int(matches.group(6)) < 0):
            raise ValueError
        else:
            end_minutes: int = 0

        end_postfix = matches.group(7)

    # if no matches - raise valueerror
    else:
        raise ValueError

    # return a string that concatenates results from two calls for am_pm_convert function
    return f"{am_pm_convert_to_24hrs(start_hours, start_minutes, start_postfix)} to {am_pm_convert_to_24hrs(end_hours, end_minutes, end_postfix)}"


# function takes 3 args: hrs, mins, AM|PM
def am_pm_convert_to_24hrs(time_hours: int, time_minutes: int, time_postfix: str) -> str:
    convert_dict = {"12:00 AM": "00:00",
                    "1:00 AM": "01:00",
                    "2:00 AM": "02:00",
                    "3:00 AM": "03:00",
                    "4:00 AM": "04:00",
                    "5:00 AM": "05:00",
                    "6:00 AM": "06:00",
                    "7:00 AM": "07:00",
                    "8:00 AM": "08:00",
                    "9:00 AM": "09:00",
                    "10:00 AM": "10:00",
                    "11:00 AM": "11:00",
                    "12:00 PM": "12:00",
                    "1:00 PM": "13:00",
                    "2:00 PM": "14:00",
                    "3:00 PM": "15:00",
                    "4:00 PM": "16:00",
                    "5:00 PM": "17:00",
                    "6:00 PM": "18:00",
                    "7:00 PM": "19:00",
                    "8:00 PM": "20:00",
                    "9:00 PM": "21:00",
                    "10:00 PM": "22:00",
                    "11:00 PM": "23:00"
                    }
    # gets 24hrs format from dictionary
    # create a string to return
    # replaces minutes (that are always equal to 00 in dict) with actual mins value
    # formats minutes to be filled with leading zeroes
    return convert_dict.get(f"{str(time_hours)}:00 {time_postfix}").replace("00", f"{time_minutes:02}")


if __name__ == "__main__":
    main()
