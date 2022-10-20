# format1 http://youtube.com/embed/xvFZjo5PgG0
# format2 https://youtube.com/embed/xvFZjo5PgG0
# format3 https://www.youtube.com/embed/xvFZjo5PgG0
# example <iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>
# return https://youtu.be/xvFZjo5PgG0
# <iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0"
# title="YouTube video player" frameborder="0" allow="accelerometer; autoplay;
# clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches := re.search(r"^.+/embed/(\w+)\".+$", s, re.IGNORECASE):
        return "https://youtu.be/" + matches.group(1)
    else:
        return None


if __name__ == "__main__":
    main()
