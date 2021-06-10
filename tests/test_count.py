
from testing.count import count 

def test_count_zero():
    assert count([0,0,0,], 0) == 3

def test_count_string():
    assert count(["a","a","a"], "a") == 3

    

