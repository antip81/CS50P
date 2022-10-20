import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # splits a string into a list based on "." separator
    numbers = re.split(r"\.", ip)
    # if len !=4 than ip addr is not valid
    if len(numbers) != 4:
        return False
    else:
        try:
            for number in numbers:
                # if ip octet decimal value > 255 - ip addr is not valid
                if int(number) > 255 or int(number) < 0:
                    return False
        except ValueError:
            return False
    return True


if __name__ == "__main__":
    main()
