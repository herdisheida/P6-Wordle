from MyComparableKey import MyComparableKey

if __name__ == "__main__":
    k1 = MyComparableKey(1, "one")
    k2a = MyComparableKey(2, "two")
    k2b = MyComparableKey(2, "two")
    k3 = MyComparableKey(1, "two")
    k4 = MyComparableKey(3, "three")
    k5 = MyComparableKey(3, "four")
    
    print(k1 < k2a)  # true     (1, "one") < (2, "two")
    print(k2b < k1)  # false    (2, "two") < (1, "one")
    print(k2a < k2b) # false    (2, "two") < (2, "two")
    print(k2b < k2a) # false    (2, "two") < (2, "two")
    print("MORE TEST \n")

    # Additional tests
    print(k1 < k3)  # true     (1, "one") < (1, "two")
    # assert k1 < k3 == True
    
    print(k3 < k1)  # false    (1, "two") < (1, "one")
    # assert k3 < k1 == False
    
    print(k4 < k5)  # false     (3, "three") < (3, "four")
    # assert k4 < k5 == False
    
    print(k5 < k4)  # True    (3, "four") < (3, "three")
    # assert k5 < k4 == True
    
    print(k1 < k4)  # true     (1, "one") < (3, "three")
    # assert k1 < k4 == True
    
    print(k4 < k1)  # false    (3, "three") < (1, "one")
    # assert k4 < k1 == False



