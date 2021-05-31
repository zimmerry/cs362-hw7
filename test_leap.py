import pytest
import leap

def test1():
    assert leap.is_leap(8) == True

def test2():
    assert leap.is_leap(200) == False

def test3():
    assert leap.is_leap(800) == True