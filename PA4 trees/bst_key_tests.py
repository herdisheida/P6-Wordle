from MyComparableKey import MyComparableKey


if __name__ == "__main__":
    k1 = MyComparableKey(1, "one")
    k2a = MyComparableKey(2, "two")
    k2b = MyComparableKey(2, "two")
    print(k1 < k2a)  # true     (1, "one") < (2, "two")
    print(k2b < k1)  # false    (2, "two") < (1, "one")
    print(k2a < k2b) # false    (2, "two") < (2, "two")
    print(k2b < k2a) # false    (2, "two") < (2, "two")
