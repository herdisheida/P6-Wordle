from skil.Bucket import Bucket, ItemExistsException, NotFoundException
from skil.HashMap import HashMap
from skil.MyHashableKey import MyHashableKey


def bucket_test():

    b = Bucket()
    assert len(b) == 0
    # remove empty
    try:
        b.remove(1)
    except NotFoundException:
        pass

    # test insert
    b.insert(5, "fimm")
    b.insert(4, "fjórir")
    b.insert(3, "þrír")
    b.insert(2, "tveir")
    b.insert(1, "einn")
    assert str(b) == "{1:einn} {2:tveir} {3:þrír} {4:fjórir} {5:fimm} "
    assert len(b) == 5

    try:
        b.insert(5, "fimmdimmalimm")
    except ItemExistsException:
        pass

    # test find - after insert
    assert b.find(1) == "einn"
    assert b.find(2) == "tveir"
    assert b.find(3) == "þrír"
    assert b.find(4) == "fjórir"
    assert b.find(5) == "fimm"

    # test linking
    assert b.head.key == 1
    assert b.head.next.key == 2
    assert b.head.next.next.key == 3
    assert b.head.next.next.next.key == 4
    assert b.head.next.next.next.next.key == 5
    # assert b.head.next.next.next.next.key == b.tail.key
    # assert b.tail.key == 5

    # test update
    b.update(1, "ás")
    b.update(2, "tvistur")
    b.update(3, "þristur")
    b.update(4, "fjarki")
    b.update(5, "fimma")
    assert str(b) == "{1:ás} {2:tvistur} {3:þristur} {4:fjarki} {5:fimma} "
    assert len(b) == 5

    # test find - after update
    assert b.find(1) == "ás"
    assert b.find(2) == "tvistur"
    assert b.find(3) == "þristur"
    assert b.find(4) == "fjarki"
    assert b.find(5) == "fimma"

    # test contains
    assert b.contains(1) == True
    assert b.contains(2) == True
    assert b.contains(3) == True
    assert b.contains(4) == True
    assert b.contains(5) == True
    assert b.contains(6) == False
    assert b.contains("YOLO") == False
    assert b.contains("HO") == False

    # test remove
    b.remove(1) # remove first
    assert str(b) == "{2:tvistur} {3:þristur} {4:fjarki} {5:fimma} "
    assert len(b) == 4
    b.remove(5) # remove last
    assert str(b) == "{2:tvistur} {3:þristur} {4:fjarki} "
    assert len(b) == 3
    b.remove(3) # remove middle
    assert str(b) == "{2:tvistur} {4:fjarki} "
    assert len(b) == 2

    # test __setitem__
    b[1] = "new ace"
    assert str(b) == "{1:new ace} {2:tvistur} {4:fjarki} "
    assert len(b) == 3
    b[2] = "twinning"
    assert str(b) == "{1:new ace} {2:twinning} {4:fjarki} "
    assert len(b) == 3
    b[4] = "fjarkalarki"
    assert str(b) == "{1:new ace} {2:twinning} {4:fjarkalarki} "
    assert len(b) == 3

    # test __getitem__
    assert b[1] == "new ace"
    assert b[2] == "twinning"
    assert b[4] == "fjarkalarki"

    # remove all
    b.remove(1)
    assert str(b) == "{2:twinning} {4:fjarkalarki} "
    assert len(b) == 2
    b.remove(2)
    assert str(b) == "{4:fjarkalarki} "
    assert len(b) == 1
    b.remove(4)
    assert str(b) == ""
    assert len(b) == 0
    try:
        b.remove(10)
    except NotFoundException:
        pass
    assert len(b) == 0

    # insert - after removing all
    b.insert(100000000, "senku")
    assert str(b) == "{100000000:senku} "
    assert len(b) == 1

    print("Bucket tests passed")

def hashMap_test():
    h = HashMap()
    assert len(h) == 0
    assert h.bucket_count == 8
    # remove empty
    try:
        h.remove(1)
    except NotFoundException:
        pass

    # test insert
    h.insert(5, "fimm")
    h.insert(4, "fjórir")
    h.insert(3, "þrír")
    h.insert(2, "tveir")
    h.insert(1, "einn")
    assert str(h) == "{1:einn} {2:tveir} {3:þrír} {4:fjórir} {5:fimm} "
    assert len(h) == 5

    try:
        h.insert(5, "fimmdimmalimm")
    except ItemExistsException:
        pass

    # test find - after insert
    assert h.find(1) == "einn"
    assert h.find(2) == "tveir"
    assert h.find(3) == "þrír"
    assert h.find(4) == "fjórir"
    assert h.find(5) == "fimm"

    # test update
    h.update(1, "ás")
    h.update(2, "tvistur")
    h.update(3, "þristur")
    h.update(4, "fjarki")
    h.update(5, "fimma")
    assert str(h) == "{1:ás} {2:tvistur} {3:þristur} {4:fjarki} {5:fimma} "
    assert len(h) == 5

    # test find - after update
    assert h.find(1) == "ás"
    assert h.find(2) == "tvistur"
    assert h.find(3) == "þristur"
    assert h.find(4) == "fjarki"
    assert h.find(5) == "fimma"

    # test contains
    assert h.contains(1) == True
    assert h.contains(2) == True
    assert h.contains(3) == True
    assert h.contains(4) == True
    assert h.contains(5) == True
    assert h.contains(6) == False
    assert h.contains("YOLO") == False
    assert h.contains("HO") == False

    # test remove
    h.remove(1) # remove first
    assert str(h) == "{2:tvistur} {3:þristur} {4:fjarki} {5:fimma} "
    assert len(h) == 4
    h.remove(5) # remove last
    assert str(h) == "{2:tvistur} {3:þristur} {4:fjarki} "
    assert len(h) == 3
    h.remove(3) # remove middle
    assert str(h) == "{2:tvistur} {4:fjarki} "
    assert len(h) == 2

    # test __setitem__
    h[1] = "new ace"
    assert str(h) == "{1:new ace} {2:tvistur} {4:fjarki} "
    assert len(h) == 3
    h[2] = "twinning"
    assert str(h) == "{1:new ace} {2:twinning} {4:fjarki} "
    assert len(h) == 3
    h[4] = "fjarkalarki"
    assert str(h) == "{1:new ace} {2:twinning} {4:fjarkalarki} "
    assert len(h) == 3

    # test __getitem__
    assert h[1] == "new ace"
    assert h[2] == "twinning"
    assert h[4] == "fjarkalarki"

    # remove all
    h.remove(1)
    assert str(h) == "{2:twinning} {4:fjarkalarki} "
    assert len(h) == 2
    h.remove(2)
    assert str(h) == "{4:fjarkalarki} "
    assert len(h) == 1
    h.remove(4)
    assert str(h) == ""
    assert len(h) == 0
    try:
        h.remove(10)
    except NotFoundException:
        pass
    assert len(h) == 0

    # insert - after removing all
    h.insert(100000000, "senku")
    assert str(h) == "{100000000:senku} "
    assert len(h) == 1



    print("HashMap tests passed")

def hashKey_test():
    k1 = MyHashableKey(1, "Hello")
    k1_copy = MyHashableKey(1, "Hello")

    k2 = MyHashableKey(2, "World")
    k2_diff = MyHashableKey(2, "Wor")
    
    k3 = MyHashableKey(3, "Wor")

    assert k1 == k1_copy, "True: same int, same str"
    # assert k1 == k2, "False: diff int, diff str"
    # assert k2 == k2_diff, "False: same int, diff str"
    # assert k3 == k2_diff, "False: diff int, same str"




if __name__ == "__main__":
    bucket_test()
    hashMap_test()

    hashKey_test()