from um import count


def main():
    test_count_words()
    test_count_symbols()
    test_count_numbers()


def test_count_words():
    assert count("Um, thanks for the album.") == 1
    assert count("um") == 1
    assert count("um?") == 1
    assert count("Um, thanks, um...") == 2
    assert count("circumstances") == 0


def test_count_symbols():
    assert count("um, um. ]um[ um= um-)(*&^%$#@!um") == 6


def test_count_numbers():
    assert count("um1, um0, um, 12345um67890") == 1


if __name__ == '__main__':
    main()
