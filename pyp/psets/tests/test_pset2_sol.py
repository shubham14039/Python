import pytest
import solutions.pset2_sol as pset2_sol

def test_divide():
    result = pset2_sol.divide(6,2)
    assert result == 3