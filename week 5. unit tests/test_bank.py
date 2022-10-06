from bank import value


def main():
    test_value_how()
    test_value_hello()
    test_value_digits()
    test_value_not_in_h()
    test_value_symbols()


def test_value_hello():
    assert value("hello") == "$0"
    assert value("     hello  ") == "$0"


def test_value_how():
    assert value("how") == "$20"
    assert value("    how    ") == "$20"


def test_value_not_in_h():
    assert value("sfvfsfgsgsf") == "$100"
    assert value("     sfvfsfgsgsf   ") == "$100"


def test_value_digits():
    assert value("1241414") == "$100"
    assert value("    1241414     ") == "$100"


def test_value_symbols():
    assert value("-=[]';./") == "$100"
    assert value("    -=[]';./     ") == "$100"


if __name__ == '__main__':
    main()
