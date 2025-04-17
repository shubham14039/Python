import pytest 
import array as arr
import source.def_based as def_based


def test_frequency():
    aray = arr.array('i',[1,2,3,4,7,2,4,3,1,9,7,6,4,8,4,3,6,7,8,9,3,2,1,5])
    result = def_based.frequency(aray)
    assert result == {1: 3, 2: 3, 3: 4, 4: 4, 7: 3, 9: 2, 6: 2, 8: 2, 5: 1}

def test_intersection():
    l = [1,2,3,4,5,6,7,8,9]
    s = [1,87,34,2,4,56,23,6]
    result = def_based.intersection(s,l)
    assert result == [1,2,4,6]






def test_reverse_array():
    pass
    result = def_based.reverse_array()


def test_twoSum():
    pass
    result = def_based.twoSum()
