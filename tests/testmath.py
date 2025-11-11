from src.math import add,subs,mult

def test_add():
    assert add(2,3) == 5
    assert add(4,4) == 8

def test_sub():
    assert subs(6,3) == 3
    assert subs(3,3) == 0

def test_mult():
    assert mult(9,9) == 81
    assert mult(5,4) == 20