def main():
    print(gauge(convert(input("Fraction: "))))


def convert(fraction: str) -> int:
    if int(fraction.split("/")[1]) == 0:
        raise ZeroDivisionError
    elif not fraction.split("/")[0].isdecimal() or not fraction.split("/")[1].isdecimal() or int(fraction.split("/")[0]) > int(fraction.split("/")[1]):
        raise ValueError
    else:
        return int(int(fraction.split("/")[0]) / int(fraction.split("/")[1]) * 100)


def gauge(percent: int) -> str:
    if percent <= 1:
        return "E"
    elif percent >= 99:
        return "F"
    else:
        return str(percent) + "%"


if __name__ == '__main__':
    main()
