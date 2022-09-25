# https://cs50.harvard.edu/python/2022/psets/3/grocery/#grocery-list
# In a file called grocery.py, implement a program that prompts the user for items,
# one per line, until the user inputs control-d (which is a common way of ending one’s input to a program).
# Then output the user’s grocery list in all uppercase, sorted alphabetically by item,
# prefixing each line with the number of times the user inputted that item.
# No need to pluralize the items. Treat the user’s input case-insensitively.

def main():
    # prints a list taken from grocery_list function
    # with revers order of items in each element
    # i.e. "APPLE 5" will be printed as "5 APPLE"
    for item in grocery_list():
        # takes last character in the string witch is amount
        # then " " then remaining string.
        # if an amount >=10 - will work incorrectly
        print("".join(item[-1:]) + " " + "".join(item[0:len(item) - 2]))

def grocery_list() -> list:
    # dictionary {item: amount of items}
    grocery_dict = {}
    # dictionary converted to a list
    grocery_dictlist = []

    while True:
        try:
            # user inputs items converted to uppercase
            item = input("item: ").upper()
            # cheks if key already exist, if not -> new key with value = 1
            if grocery_dict.get(item) == None:
                grocery_dict.update({item: 1})
            # if key already exist -> updates the value to +1
            else:
                grocery_dict[item] = grocery_dict.get(item) + 1
        # ctrl+d means end of user input
        except EOFError:
            # makes empty string
            print('')
            break
    # debug
    # print("grocery_dict", grocery_dict)

    # procedure to convert dict to a list
    for key, value in grocery_dict.items():
        temp_list = [key, value]
        item = ""

        # removes [],' symbols from temp_list
        for char in str(temp_list):
            if char not in "[,']":
                item = item + char
            else:
                pass
        # append item to grocery_dictlist
        grocery_dictlist.append(item)

    # sort list in asc order
    grocery_dictlist.sort()

    # debug
    # print("grocery_dictlist ", grocery_dictlist)
    return grocery_dictlist


main()