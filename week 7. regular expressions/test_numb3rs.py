from numb3rs import validate


def main():
    test_validate_correct_addr()
    test_validate_hollow()
    test_validate_letters()
    test_validate_num_out_of_range()
    test_validate_negative_num()


def test_validate_correct_addr():
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("10.10.10.10") == True
    assert validate("10.0.0.0") == True
    assert validate("0.10.0.0") == True
    assert validate("0.0.10.0") == True
    assert validate("0.0.0.10") == True


def test_validate_letters():
    assert validate("a.0.0.0") == False
    assert validate("0.a.0.0") == False
    assert validate("0.0.a.0") == False
    assert validate("0.0.0.a") == False


def test_validate_hollow():
    assert validate("0.0.0.") == False
    assert validate("0.0..0") == False
    assert validate("0..0.0") == False
    assert validate(".0.0.0") == False


def test_validate_num_out_of_range():
    assert validate("256.0.0.0") == False
    assert validate("0.256.0.0") == False
    assert validate("0.0.256.0") == False
    assert validate("0.0.0.256") == False


def test_validate_negative_num():
    assert validate("-1.0.0.0") == False
    assert validate("0.-1.0.0") == False
    assert validate("0.0.-1.0") == False
    assert validate("0.0.0.-1") == False


if __name__ == '__main__':
    main()
