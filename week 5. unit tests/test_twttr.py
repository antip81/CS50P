from twttr import shorten


def main():
    test_shorten_vowels()
    test_shorten_non_vowels()
    test_shorten_numbers()


def test_shorten_vowels():
    assert shorten("aeiouAEIOU") == ""


def test_shorten_numbers():
    assert shorten("1234567890-=[];/., ") == "1234567890-=[];/., "


def test_shorten_non_vowels():
    assert shorten("qwrtpsdfghjklzxcvbnmQWRTPSDFGHJKLZXCVBNM") == "qwrtpsdfghjklzxcvbnmQWRTPSDFGHJKLZXCVBNM"


if __name__ == '__main__':
    main()
