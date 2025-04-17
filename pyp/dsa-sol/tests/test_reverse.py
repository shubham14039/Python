import pytest
import source.reverse as reverse

def test_reverse():
    result = reverse.reverse_items([0,1,2,3,4,5,6,7,8,9])
    assert result == [9,8,7,6,5,4,3,2,1,0]