from array_list import ArrayList, IndexOutOfBounds, Empty, NotFound, NotOrdered


def main():
    arr_lis = ArrayList()

    # Test: Initial state
    assert arr_lis.size == 0, "The list should start empty"
    assert arr_lis.capacity == 3, "The list should start with a capacity of 3"
    assert str(arr_lis) == ""

    # Test: Append and Prepend
    # Appending an empty list
    arr_lis.append(1)
    assert str(arr_lis) == "1"
    arr_lis.prepend(0)
    assert str(arr_lis) == "0, 1"
    # Test: Append and Prepend
    # Prepending an empty list
    arr_lis.clear()  # Clear the list for next test
    arr_lis.prepend(0)
    assert str(arr_lis) == "0"
    arr_lis.append(1)
    assert str(arr_lis) == "0, 1"

    # Test: Insert
    # Inserting into an empty list
    arr_lis.clear()  # Clear the list for next test

    try:  # inserting into an empty list not at index 0
        arr_lis.insert(1, 1)
    except IndexOutOfBounds:
        pass
    else:
        assert False, "Expected IndexOutOfBounds exception"
    try:  # inserting at a negative index
        arr_lis.insert(1, -1)
    except IndexOutOfBounds:
        pass
    else:
        assert False, "Expected IndexOutOfBounds exception"

    arr_lis.insert(0, 0)
    assert str(arr_lis) == "0"

    # Test: Insert
    # Inserting into a list with elements
    arr_lis.insert(1, 1)
    assert str(arr_lis) == "0, 1"
    assert arr_lis.is_ordered == False, "The list should be unordered"

    arr_lis.insert(2, 2)
    assert str(arr_lis) == "0, 1, 2"
    arr_lis.insert(1.5, 2)
    assert str(arr_lis) == "0, 1, 1.5, 2"

    # Test: Set at
    arr_lis.set_at(3, 3)  # set at the end
    assert str(arr_lis) == "0, 1, 1.5, 3"
    arr_lis.set_at(2, 1)  # set at the middle
    assert str(arr_lis) == "0, 2, 1.5, 3"
    arr_lis.set_at(10, 0)  # set at the beginning
    assert str(arr_lis) == "10, 2, 1.5, 3"

    # Test: Get first, at, last
    assert arr_lis.get_first() == 10
    assert arr_lis.get_at(0) == 10  # get at the beginning
    assert arr_lis.get_at(1) == 2  # get at the middle
    assert arr_lis.get_at(3) == 3  # get at the end
    assert arr_lis.get_last() == 3

    # Test: Remove at
    arr_lis.remove_at(0)  # remove at the beginning
    assert str(arr_lis) == "2, 1.5, 3"
    assert arr_lis.is_ordered == False, "The list should be unordered"
    arr_lis.remove_at(1)  # remove at the middle
    assert str(arr_lis) == "2, 3"
    assert arr_lis.is_ordered == False, "The list should be unordered"
    arr_lis.remove_at(1)  # remove at the end
    assert str(arr_lis) == "2"
    assert arr_lis.is_ordered == False, "The list should be unordered"
    arr_lis.remove_at(0)  # remove the last element
    assert str(arr_lis) == ""
    assert arr_lis.is_ordered == False, "The list should be unordered"


    try:  # remove at a negative index
        arr_lis.remove_at(-1)
    except IndexOutOfBounds:
        pass
    else:
        assert False, "Expected IndexOutOfBounds exception"
    try:  # remove at an index greater than the size
        arr_lis.remove_at(2)
    except IndexOutOfBounds:
        pass

    # Test: Clear
    arr_lis.clear()
    assert arr_lis.size == 0
    assert str(arr_lis) == ""
    assert arr_lis.is_ordered == False

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




    # Test: insert_ordered() and find() in ordered lists
    new_arr_lis = ArrayList()

    new_arr_lis.insert_ordered(10)
    assert str(new_arr_lis) == "10"
    new_arr_lis.insert_ordered(20)  # insert larger
    assert str(new_arr_lis) == "10, 20"
    new_arr_lis.insert_ordered(15)  # insert in the middle
    assert str(new_arr_lis) == "10, 15, 20"
    new_arr_lis.insert_ordered(5)  # insert smaller
    assert str(new_arr_lis) == "5, 10, 15, 20"
    new_arr_lis.insert_ordered(15)  # insert equal to another element
    assert str(new_arr_lis) == "5, 10, 15, 15, 20"


        # TEST: find() in ordered lists
    assert new_arr_lis.is_ordered == True
    assert new_arr_lis.find(5) == 0
    assert new_arr_lis.find(10) == 1
    assert new_arr_lis.find(15) == 2
    assert new_arr_lis.find(20) == 4

    try:  # find value which is not in the list
        new_arr_lis.find(100)
    except NotFound:
        pass
    else:
        assert False, "Expected NotFound exception"




    # Test: insert_ordered and find() in unordered lists
        # into an unordered list
        # make the list unordered with Append/Prepend/Set_at/Insert


            # 1. make list unordered with Append
    new_arr_lis.append(999)
    assert str(new_arr_lis) == "5, 10, 15, 15, 20, 999"
    assert new_arr_lis.is_ordered == False
            # 2. make list unordered with Prepend
    # new_arr_lis.prepend(999)
    # assert str(new_arr_lis) == "999, 5, 10, 15, 15, 20"
    # assert new_arr_lis.is_ordered == False
            # 3. make list unordered with Set_at
    # new_arr_lis.set_at(999, 0)
    # assert str(new_arr_lis) == "999, 10, 15, 15, 20"
    # assert new_arr_lis.is_ordered == False
            # 4. make list unordered with Insert
    # new_arr_lis.insert(999, 1)
    # assert str(new_arr_lis) == "5, 999, 10, 15, 15, 20"
    # assert new_arr_lis.is_ordered == False

    try: # insert_ordered into an unordered list
        new_arr_lis.insert_ordered(1000)
    except NotOrdered:
        pass
    else:
        assert False, "Expected NotOrdered exception"

        # Test: find() in unordered lists
    assert new_arr_lis.find(5) == 0
    assert new_arr_lis.find(10) == 1
    assert new_arr_lis.find(15) == 2
    assert new_arr_lis.find(20) == 4
    assert new_arr_lis.find(999) == 5

    try:  # find value which is not in the list
        new_arr_lis.find(-100)
    except NotFound:
        pass
    else:
        assert False, "Expected NotFound exception"



    # TEST: remove_value()
    new_arr_lis.remove_value(5)
    assert str(new_arr_lis) == "10, 15, 15, 20, 999" # remove at the beginning
    new_arr_lis.remove_value(20)
    assert str(new_arr_lis) == "10, 15, 15, 999" # remove in the middle
    new_arr_lis.remove_value(999)
    assert str(new_arr_lis) == "10, 15, 15" # remove at the end
    new_arr_lis.remove_value(15)
    assert str(new_arr_lis) == "10, 15" # remove doublicates


    arr_list_empty = ArrayList()
    try:  # remove value from an empty list
        arr_list_empty.remove_value(10)
    except NotFound:
        pass
    else:
        assert False, "Expected NotFound exception"


    print("All tests passed! :D")


if __name__ == "__main__":
    main()
