from array_list import ArrayList, IndexOutOfBounds, Empty, NotFound, NotOrdered


if __name__ == "__main__":

    arr_lis = ArrayList()

    print("\n   ALL CLEARED: ")
    arr_lis.clear()
    print("Size:      ", arr_lis.size)
    print("Capacity:  ", arr_lis.capacity)
    print("Array:     ", arr_lis, "\n")

    
        
    # TEST: add to list
    arr_lis.append("append 1 HERE")
    print(arr_lis)

    arr_lis.prepend("prepend 1 HERE")
    print(arr_lis)

    arr_lis.append("append 2 HERE")
    print(arr_lis)
    # arr_lis.prepend("prepend 2 HERE")
    # print(arr_lis)

    arr_lis.insert("insert at 0", 0)
    print(arr_lis)
    arr_lis.insert("insert at 3", 3)
    print(arr_lis)
    arr_lis.set_at("set at 0", 0)
    print(arr_lis)



    # TEST: get elements
    # x = arr_lis.get_first()
    # print(x)
    # x = arr_lis.get_at(0)
    # print(x)
    # x = arr_lis.get_last()
    # print(x)

    # TEST: remove
    arr_lis.remove_at(0)
    print("remove at 0: ", arr_lis)



    # print("\n   ALL CLEARED: ")
    # arr_lis.clear()
    # print("Size:      ", arr_lis.size)
    # print("Capacity:  ", arr_lis.capacity)
    # print("Array:     ", arr_lis, "\n")

    arr_lis1 = ArrayList()
    arr_lis1.insert(124, 0)
    print(arr_lis1)
    arr_lis1.insert(256, 1)
    print(arr_lis1)



    # TEST : insert_ordered
    arr_lis2 = ArrayList()

    arr_lis2.insert_ordered(10)
    print(arr_lis2)
    arr_lis2.insert_ordered(562)
    print(arr_lis2)
    arr_lis2.insert_ordered(200)
    print(arr_lis2)
    arr_lis2.insert_ordered(200)
    print(arr_lis2)
    arr_lis2.insert_ordered(300)
    print(arr_lis2)
    arr_lis2.insert_ordered(600)
    print(arr_lis2)
    arr_lis2.insert_ordered(800)
    print(arr_lis2)

    # test find in ordered lists
    assert arr_lis2.is_ordered == True
    print(arr_lis2.find(10)) # 0
    print(arr_lis2.find(200)) # 1
    print(arr_lis2.find(300)) # 3
    print(arr_lis2.find(562)) # 4
    print(arr_lis2.find(600)) # 5
    print(arr_lis2.find(800)) # 6

    try: # find smth that is not an element in the ordered list
        arr_lis2.find(9231483490)
    except NotFound:
        pass
    else:
        assert False, "Expected NotFound exception"

    # test find in unordered lists
    arr_lis2.append(999) # making list unordered
    print(arr_lis2)
    assert arr_lis2.is_ordered == False
    print(arr_lis2.find(10)) # 0
    print(arr_lis2.find(200)) # 1
    print(arr_lis2.find(300)) # 3
    print(arr_lis2.find(562)) # 4
    print(arr_lis2.find(600)) # 5
    print(arr_lis2.find(800)) # 6
    print(arr_lis2.find(999)) # 7

    try: # find smth that is not an element in the unordred list
        arr_lis2.find(9231483490)
    except NotFound:
        pass
    else:
        assert False, "Expected NotFound exception"



    # TEST: remove_value
    arr_lis2.remove_value(10) # remove first element
    print(arr_lis2)
    arr_lis2.remove_value(300) # remove middle element
    print(arr_lis2)
    arr_lis2.remove_value(200) # remove doublicate element
    print(arr_lis2)
    arr_lis2.remove_value(999) # remove last element
    print(arr_lis2)