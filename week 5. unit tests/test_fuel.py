from fuel import convert, gauge
import pytest


def main():
    test_convert_values()
    test_convert_errors()
    test_gauge()


def test_convert_values():
    assert convert("3/4") == 75
    assert convert("4/4") == 100
    assert convert("0/4") == 0


def test_convert_errors():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ValueError):
        convert("4/3")
    with pytest.raises(ValueError):
        convert("a/4")
    with pytest.raises(ValueError):
        convert("4/a")


def test_gauge():
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(75) == "75%"


if __name__ == '__main__':
    main()
