import fizzbuzz
import pytest

def test_first_line(capsys):
    fizzbuzz.fizzbuzz()

    output = capsys.readouterr().out.split('\n')[:-1]
    assert output[0] == "1"