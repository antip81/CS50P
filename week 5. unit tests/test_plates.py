from plates import is_valid


def main():
    test_is_valid_numbers()
    test_is_valid_len()
    test_is_valid_zero()
    test_is_valid_symbols()


def test_is_valid_len():
    assert is_valid("a") == False
    assert is_valid("ab") == True
    assert is_valid("abc") == True
    assert is_valid("abcd") == True
    assert is_valid("abcde") == True
    assert is_valid("abcdef") == True
    assert is_valid("abcdefg") == False


def test_is_valid_numbers():
    assert is_valid("AA3456") == True
    assert is_valid("A23456") == False
    assert is_valid("AA23AA") == False


def test_is_valid_zero():
    assert is_valid("AA0456") == False
    assert is_valid("AA3056") == True


def test_is_valid_symbols():
    assert is_valid("AA34 6") == False
    assert is_valid("AA34,6") == False
    assert is_valid("AA34.6") == False


if __name__ == '__main__':
    main()