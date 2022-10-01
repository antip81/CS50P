# https://cs50.harvard.edu/python/2022/psets/4/bitcoin/

import requests
import sys


def main():
    cost = get_cli_input() * get_usd_rate()
    # prints cost in a format of $12,345.67
    print(f"${cost:,.4f}")


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
def get_usd_rate() -> float:
    # makes request to an url and converts to json
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').json()

    # gets a value for rate_float in "bpi" "USD" "rate" key in r dict
    return float(r["bpi"]["USD"]["rate_float"])


if __name__ == '__main__':
    main()
