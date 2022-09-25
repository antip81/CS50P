# https://cs50.harvard.edu/python/2022/psets/3/grocery/#grocery-list

def main():
    grocery_list: dict[str, int] = {}

    while True:
        try:
            item: str = input("Item: ").strip()
            # adds/replaces dict element: item as a key
            # value = get current value + 1
            # if there is no current value return 0 and +1
            grocery_list[item] = grocery_list.get(item, 0) + 1
        except EOFError:
            print()
            break
    print(grocery_list)

    # for each item in sorted dict
    # print value and key
    for item in sorted(grocery_list):
        print(grocery_list[item], item.upper())


main()