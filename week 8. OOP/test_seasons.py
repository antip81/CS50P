from seasons import how_old_in_minutes
import pytest


def main():
    test_hoim_value_errors()


def test_hoim_value_errors():
    with pytest.raises(SystemExit):
        how_old_in_minutes("January 1, 1999")
    with pytest.raises(SystemExit):
        how_old_in_minutes("111-12-12")
    with pytest.raises(SystemExit):
        how_old_in_minutes("1111-13-12")
    with pytest.raises(SystemExit):
        how_old_in_minutes("1111-12-32")


if __name__ == "__main__":
    main()
