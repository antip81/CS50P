def main():
    text = input("Input: ")
    print(remove_vowels(text))


def remove_vowels(string):
    result = ""
    for char in string:
        if char not in "aeiouAEIOU":
            result = result + char
    return result

main()
