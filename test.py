from ArrayList import ArrayList, IndexOutOfBounds, Empty

def main():
    arr_lis = ArrayList()

    # Test: Initial state
    assert arr_lis.size == 0, "The list should start empty"
    assert arr_lis.capacity == 3
    assert str(arr_lis) == "The Array is empty"

    # Test: Append and Prepend
    arr_lis.append(1)
    assert str(arr_lis) == "1"
    arr_lis.prepend(0)
    assert str(arr_lis) == "0, 1"

    # Test: Insert
    arr_lis.insert(2, 2)
    assert str(arr_lis) == "0, 1, 2"
    arr_lis.insert(1.5, 2)
    assert str(arr_lis) == "0, 1, 1.5, 2"

    # Test: Set at
    arr_lis.set_at(3, 3)
    assert str(arr_lis) == "0, 1, 1.5, 3"

    # Test: Get first, at, last
    assert arr_lis.get_first() == 0
    assert arr_lis.get_at(1) == 1
    assert arr_lis.get_last() == 3

    # Test: Remove at
    arr_lis.remove_at(1)
    assert str(arr_lis) == "0, 1.5, 3"

    # Test: Clear
    arr_lis.clear()
    assert arr_lis.size == 0
    assert str(arr_lis) == "The Array is empty"



    # Test: Edge cases
    try:
        arr_lis.get_first()
    except Empty:
        pass
    else:
        assert False, "Expected Empty exception"

    try:
        arr_lis.get_at(0)
    except IndexOutOfBounds:
        pass
    else:
        assert False, "Expected IndexOutOfBounds exception"

    try:
        arr_lis.get_last()
    except Empty:
        pass
    else:
        assert False, "Expected Empty exception"

    try:
        arr_lis.set_at(1, 0)
    except IndexOutOfBounds:
        pass
    else:
        assert False, "Expected IndexOutOfBounds exception"

    try:
        arr_lis.remove_at(0)
    except IndexOutOfBounds:
        pass
    else:
        assert False, "Expected IndexOutOfBounds exception"

    print("All tests passed! :D")

if __name__ == "__main__":
    main()
