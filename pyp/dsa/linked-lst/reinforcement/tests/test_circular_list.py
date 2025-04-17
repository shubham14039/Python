
import pytest
import source.circular_list as CircularList


# from circular_list import CircularList  # Import the class to be tested

@pytest.fixture
def circular_list():
    """Fixture to create a new CircularList instance for each test."""
    cl = CircularList()
    return cl

def test_add(circular_list):
    circular_list.add(10)
    circular_list.add(20)
    circular_list.add(30)
    assert circular_list.printList() == [10, 20, 30]

def test_remove(circular_list):
    circular_list.add(10)
    circular_list.add(20)
    circular_list.add(30)
    
    circular_list.remove(20)  # Removing an existing element
    assert circular_list.printList() == [10, 30]
    
    circular_list.remove(50)  # Trying to remove a non-existent element
    assert circular_list.printList() == [10, 30]  # List should remain unchanged

def test_delete(circular_list):
    circular_list.add(10)
    circular_list.add(20)
    circular_list.add(30)

    circular_list.delete()  # Remove the first element (FIFO)
    assert circular_list.printList() == [20, 30]

    circular_list.delete()  # Remove next element
    assert circular_list.printList() == [30]

    circular_list.delete()  # Remove last element
    assert circular_list.printList() == []

def test_print_empty_list(circular_list, capsys):
    """Test printing an empty list."""
    circular_list.printList()
    captured = capsys.readouterr()
    assert captured.out.strip() == ""

def test_remove_from_empty_list(circular_list):
    circular_list.remove(10)  # Removing from an empty list should do nothing
    assert circular_list.printList() == []

def test_delete_from_empty_list(circular_list):
    circular_list.delete()  # Deleting from an empty list should do nothing
    assert circular_list.printList() == []

