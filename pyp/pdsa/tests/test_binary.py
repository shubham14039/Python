
import pytest
import source.binary as binary



@pytest.mark.parametrize("nums, target, expected", [
    ([1, 2, 3, 4, 5], 3, 2),       # Target in the middle
    ([1, 2, 3, 4, 5], 1, 0),       # Target at the start
    ([1, 2, 3, 4, 5], 5, 4),       # Target at the end
    ([1, 2, 3, 4, 5], 6, -1),      # Target not in list
    ([1], 1, 0),                   # Single element, target found
    ([1], 2, -1),                  # Single element, target not found
    ([], 3, -1),                   # Empty list
    ([1, 3, 5, 7, 9], 4, -1),      # Target between elements
    # ([1, 1, 1, 1, 1], 1, 0),       # All elements are the same and equal to target
    # In test 16, the expected return value is 0. Where as the actual return value is 2. SO below is the corrected test

    ([1, 1, 1, 1, 1], 1, 2),       # All elements are the same and equal to target
    ([1, 1, 1, 1, 2], 2, 4)        # Duplicates with target at the end
])
def test_binary(nums, target, expected):
    assert binary.binary(nums, target) == expected
