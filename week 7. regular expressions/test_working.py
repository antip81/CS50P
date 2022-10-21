from working import convert
import pytest
from working import am_pm_convert_to_24hrs


def main():
    test_convert()
    test_convert_value_errors()
    test_am_pm_func()


def test_convert():
    assert convert("10 AM to 9 PM") == "10:00 to 21:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"


def test_convert_value_errors():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")


def test_am_pm_func():
    assert am_pm_convert_to_24hrs(1, 10, "PM") == "13:10"
    assert am_pm_convert_to_24hrs(1, 10, "AM") == "01:10"


if __name__ == '__main__':
    main()
