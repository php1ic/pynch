from pynch.parse import Parse


def test_read_as_int():
    Parser = Parse()

    line = "123456789"
    assert Parser._read_as_int(line, 0, 2) == 12
    assert Parser._read_as_int(line, 5, len(line)) == 6789
    assert Parser._read_as_int(line, 3, 4) == 4

    assert not Parser._read_as_int("", 3, 6)
    assert Parser._read_as_int("  345    ", 0, len("  345    ")) == 345


def test_read_as_float():
    Parser = Parse()

    line = "1.23456789"
    assert Parser._read_as_float(line, 0, 2) == 1.0
    assert Parser._read_as_float(line, 0, 3) == 1.2
    assert Parser._read_as_float(line, 0, 6) == 1.2345

    assert not Parser._read_as_float("*", 0, len("*"))
    assert not Parser._read_as_float("  *  ", 0, len("  *  "))


def test_read_as_substring():
    Parser = Parse()

    line = "Some information in a string"
    assert Parser._read_substring(line, 0, 4) == "Some"
    assert not Parser._read_substring(line, 4, 5)
    assert not Parser._read_substring(" ", 0, 5)
