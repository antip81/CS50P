def main():
    text = input("Input: ").strip()
    print(f"Output: {shorten(text)}")


def shorten(string: str) -> str:
    result = ""
    for char in string:
        if char not in "aeiouAEIOU":
            result += char
    return result


if __name__ == "__main__":
    main()
