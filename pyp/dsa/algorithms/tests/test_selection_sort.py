
import pytest
import random
import source.selection as selection


def test_selection_sort_empty():
    # Sorting an empty list   
    assert selection.selection_sort([]) == []
 

def test_selection_sort_single_element():
    # sorting a list with a single element 
    assert selection.selection_sort([42]) == [42]

def test_selection_sort_two_elements():
    # sorting a list with two elements
    assert selection.selection_sort([10, 2]) == [2, 10]
    assert selection.selection_sort([2, 10]) == [2, 10]

def test_selection_sort_sorted():
    # sorting a list containing a range of elements
    arr = list(range(1000))
    sorted_arr = list(range(1000))
    assert selection.selection_sort(arr) == sorted_arr

def test_selection_sort_reverse_sorted():
    # Sorting a list in a range in reverce order
    arr = list(range(1000, 0, -1))
    sorted_arr = list(range(1, 1001))
    assert selection.selection_sort(arr) == sorted_arr

def test_selection_sort_duplicates():
    # Sorting a list containing duplicates
    arr = [5, 1, 5, 3, 2, 1, 5]
    assert selection.selection_sort(arr) == [1, 1, 2, 3, 5, 5, 5]

def test_selection_sort_negative_numbers():
    # sorting a list containing negative numbers
    arr = [0, -10, 5, -3, 2, 1, -2]
    assert selection.selection_sort(arr) == [-10, -3, -2, 0, 1, 2, 5]

def test_selection_sort_large_input():
    # sorting a list containing random numbers 
    arr = random.sample(range(1, 1000000), 10000)  # Random large input
    assert selection.selection_sort(arr) == sorted(arr)

def test_selection_sort_large_duplicates():
    # Sorting a list containing a large number of duplicates
    arr = [42] * 10000  # List with 10000 duplicate elements
    assert selection.selection_sort(arr) == [42] * 10000

def test_selection_sort_floats():
    # Sorting a list containing floating point numbers
    arr = [1.5, 3.2, -2.1, 0.0, -3.5, 2.7]
    assert selection.selection_sort(arr) == [-3.5, -2.1, 0.0, 1.5, 2.7, 3.2]

def test_selection_sort_mixed_integers_floats():
    # Sorting a list containig mix of floats and integers
    arr = [1, 3.2, -2, 0, -3.5, 2.7]
    assert selection.selection_sort(arr) == [-3.5, -2, 0, 1, 2.7, 3.2]
