import fizzbuzz
import pytest

def test_first_line(capsys):
    fizzbuzz.fizzbuzz()

    output = capsys.readouterr().out.split('\n')[:-1]
    assert output[0] == "1"

def test_third_line(capsys):
    fizzbuzz.fizzbuzz()

    output = capsys.readouterr().out.split('\n')[:-1]
    assert output[2] == "Fizz"

def test_fifth_line(capsys):
    fizzbuzz.fizzbuzz()

    output = capsys.readouterr().out.split('\n')[:-1]
    assert output[4] == "Buzz"

def test_fifteeenth_line(capsys):
    fizzbuzz.fizzbuzz()

    output = capsys.readouterr().out.split('\n')[:-1]
    assert output[14] == "FizzBuzz"