import pytest
import source.module as module


def test_mult():
    result = module.mult(5,2)
    assert result == 10

def test_divide():
    result = module.divide(10, 5)
    assert result == 2

def test_convert():
    result = module.convert(['1', '2', '4'])
    assert result == ('1', '2', '4')

