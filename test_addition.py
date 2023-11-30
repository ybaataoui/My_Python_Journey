import addition
import pytest 

def test_add():
    assert addition.add(1,2) == 3

def test_sub():
    assert addition.sub(4, 5) == -1