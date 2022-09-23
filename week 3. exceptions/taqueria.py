# In a file called taqueria.py, implement a program that enables a user to place an order,
# prompting them for items, one per line, until the user inputs control-d (which is a common way
# of ending one’s input to a program). After each inputted item, display the total cost of all items
# inputted thus far, prefixed with a dollar sign ($) and formatted to two decimal places.
# Treat the user’s input case insensitively. Ignore any input that isn’t an item.
# Assume that every item on the menu will be titlecased.

def main():
    order_placement()


def order_placement():
    menu ={
            "Baja Taco": 4.00,
            "Burrito": 7.50,
            "Bowl": 8.50,
            "Nachos": 11.00,
            "Quesadilla": 8.50,
            "Super Burrito": 8.50,
            "Super Quesadilla": 9.50,
            "Taco": 3.00,
            "Tortilla Salad": 8.00
        }
    summ = 0.00

    while True:
        try:
            # requests an item and makes it title
            item = input("Item: ").title()
            # if there is a position in menu
            if menu.get(item) != None:
                # iterate a summ variable with item price
                summ = summ + menu.get(item)
                # print summ with two decimals
                print("Total: $%.2f" %summ)
        # break if ctrl+d detected
        except EOFError:
            break


main()