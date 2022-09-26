# https://cs50.harvard.edu/python/2022/psets/4/emojize/

import emoji

def main():
    text = input("Input: ")
    print("Output:", emoji.emojize(text, language="alias"))

if __name__ == '__main__':
    main()