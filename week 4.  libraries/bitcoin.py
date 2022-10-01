# https://cs50.harvard.edu/python/2022/psets/4/bitcoin/

import requests
import locale
import sys


def main():
    # sets up an en_US for locale
    locale.setlocale(locale.LC_ALL, 'en_US')

    # calls get_cli_input and converts to str
    # calls get_usd_rate
    # uses locale.atof function to convert strs to float and multiply them
    cost = locale.atof(str(get_cli_input())) * locale.atof(get_usd_rate())
    # uses locale.currency to make format like $12,345.67
    print(locale.currency(cost, grouping=True))


# function to get cli arguments
def get_cli_input() -> float:
    # if there is no arguments given -> raise an error
    if len(sys.argv) == 1:
        sys.exit("Missing CLI argument")
    # if there is only one arg given
    elif len(sys.argv) == 2:
        try:
            # tries to use float function if successful -> return the value
            return float(sys.argv[1])
        # if ValueError - raise an error
        except ValueError:
            sys.exit("CLI argument is not a number")
    else:
        sys.exit("Too many CLI arguments")

# function to get rate in USD for 1 bitcoin
def get_usd_rate() -> str:
    # makes request to an url and stores a response in r
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    # converts r to json
    o = r.json()
    # gets a value for "bpi" key in dict
    # gets a value for "USD" key in bpi dict
    # gets a value for "rate" key in USD dict
    # and returns it as a string

    return o.get("bpi").get("USD").get("rate")


if __name__ == '__main__':
    main()
