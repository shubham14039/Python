
import pytest
import time
from source.strings import repeated_concatenation, appending_temp_list, list_comp, gen_comp

# Test for repeated_concatenation function
def test_repeated_concatenation():
    start_time = time.time()  # Start timer
    result = repeated_concatenation("abc123")
    end_time = time.time()  # End timer
    print(f"repeated_concatenation execution time: {end_time - start_time:.6f} seconds")
    assert result == "abc"
    
    start_time = time.time()
    result = repeated_concatenation("!@#ABC")
    end_time = time.time()
    print(f"repeated_concatenation execution time: {end_time - start_time:.6f} seconds")
    assert result == "ABC"

    start_time = time.time()
    result = repeated_concatenation("123456")
    end_time = time.time()
    print(f"repeated_concatenation execution time: {end_time - start_time:.6f} seconds")
    assert result == ""

    start_time = time.time()
    result = repeated_concatenation("")
    end_time = time.time()
    print(f"repeated_concatenation execution time: {end_time - start_time:.6f} seconds")
    assert result == ""  # Edge case for empty string

# Test for appending_temp_list function
def test_appending_temp_list():
    start_time = time.time()
    result = appending_temp_list("abc123")
    end_time = time.time()
    print(f"appending_temp_list execution time: {end_time - start_time:.6f} seconds")
    assert result == "a b c"

    start_time = time.time()
    result = appending_temp_list("!@#ABC")
    end_time = time.time()
    print(f"appending_temp_list execution time: {end_time - start_time:.6f} seconds")
    assert result == "A B C"

    start_time = time.time()
    result = appending_temp_list("123456")
    end_time = time.time()
    print(f"appending_temp_list execution time: {end_time - start_time:.6f} seconds")
    assert result == ""

    start_time = time.time()
    result = appending_temp_list("")
    end_time = time.time()
    print(f"appending_temp_list execution time: {end_time - start_time:.6f} seconds")
    assert result == ""  # Edge case for empty string

# Test for list_comp function
def test_list_comp():
    start_time = time.time()
    result = list_comp("abc123")
    end_time = time.time()
    print(f"list_comp execution time: {end_time - start_time:.6f} seconds")
    assert result == "abc"

    start_time = time.time()
    result = list_comp("!@#ABC")
    end_time = time.time()
    print(f"list_comp execution time: {end_time - start_time:.6f} seconds")
    assert result == "ABC"

    start_time = time.time()
    result = list_comp("123456")
    end_time = time.time()
    print(f"list_comp execution time: {end_time - start_time:.6f} seconds")
    assert result == ""

    start_time = time.time()
    result = list_comp("")
    end_time = time.time()
    print(f"list_comp execution time: {end_time - start_time:.6f} seconds")
    assert result == ""  # Edge case for empty string

# Test for gen_comp function
def test_gen_comp():
    start_time = time.time()
    result = gen_comp("abc123")
    end_time = time.time()
    print(f"gen_comp execution time: {end_time - start_time:.6f} seconds")
    assert result == ['a', 'b', 'c']

    start_time = time.time()
    result = gen_comp("!@#ABC")
    end_time = time.time()
    print(f"gen_comp execution time: {end_time - start_time:.6f} seconds")
    assert result == ['A', 'B', 'C']

    start_time = time.time()
    result = gen_comp("123456")
    end_time = time.time()
    print(f"gen_comp execution time: {end_time - start_time:.6f} seconds")
    assert result == []

    start_time = time.time()
    result = gen_comp("")
    end_time = time.time()
    print(f"gen_comp execution time: {end_time - start_time:.6f} seconds")
    assert result == []  # Edge case for empty string



