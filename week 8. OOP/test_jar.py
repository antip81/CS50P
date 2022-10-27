from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert jar.capacity == 12

    with pytest.raises(ValueError):
        jar = Jar(0)
    with pytest.raises(ValueError):
        jar = Jar(-1)
    with pytest.raises(ValueError):
        jar = Jar(3.4)

    jar = Jar(20)
    assert jar.capacity == 20


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
    jar.withdraw(4)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪"
    jar.withdraw(8)
    assert str(jar) == ""


def test_deposit():
    jar = Jar()
    jar.capacity = 10
    with pytest.raises(ValueError):
        jar.deposit(11)
    with pytest.raises(ValueError):
        jar.deposit(-1)
    with pytest.raises(ValueError):
        jar.deposit(0)


def test_withdraw():
    jar = Jar()
    jar.capacity = 10
    jar.size = 10
    with pytest.raises(ValueError):
        jar.withdraw(11)
    with pytest.raises(ValueError):
        jar.withdraw(0)
    with pytest.raises(ValueError):
        jar.withdraw(-1)


def test_is_positive_int():
    n = 1
    assert Jar.is_positive_int(n) == True
    n = 1.0
    assert Jar.is_positive_int(n) == True
    n = 1.1
    assert Jar.is_positive_int(n) == False
    n = -1
    assert Jar.is_positive_int(n) == False

