def modulus(a, b):  # ONLY NEEDS TO WORK FOR POSITIVE INTEGERS
    # base step:
    if a == 0 or a == b:
        return 0

    # inductive step:
    if a < b:
        return a
    else:
        return modulus(a - b, b)


def how_many(lis1, lis2):

    # base case
    if lis1 == [] or lis2 == []:
        return 0

    # inductive step
    first = lis1[0]
    rest = lis1[1:]

    if first in lis2:
        # count when an element is found
        return 1 + how_many(rest, lis2)
    return how_many(rest, lis2)


# FEEL FREE TO EDIT THE TESTS AND MAKE THEM BETTER
# REMEMBER EDGE CASES!


def test_modulus(num1, num2):
    print("The modulus of " + str(num1)+ " and " + str(num2) + " is " + str(modulus(num1, num2)))


def test_how_many(lis1, lis2):
    print(str(how_many(lis1, lis2)) + " of the items in " + str(lis1)+ " are also in " + str(lis2))


def run_recursion_program():

    print("\nTESTING MODULUS:\n")

    test_modulus(8, 3)
    test_modulus(9, 3)
    test_modulus(10, 3)
    test_modulus(11, 3)
    test_modulus(8, 2)
    test_modulus(0, 7)
    test_modulus(15, 5)
    test_modulus(128, 16)
    test_modulus(128, 15)

    # MY TESTS
    # assert modulus(8, 3) == 2
    # assert modulus(9, 3) == 0
    # assert modulus(10, 3) == 1
    # assert modulus(11, 3) == 2
    # assert modulus(8, 2) == 0
    # assert modulus(0, 7) == 0
    # assert modulus(15, 5) == 0
    # assert modulus(128, 16) ==  0
    # assert modulus(128, 15) ==  8

    # assert modulus(1, 1) == 0
    # assert modulus(1, 2) == 1
    # assert modulus(2, 1) == 0
    # assert modulus(15, 128) == 15
    # print("------ MODULUS TESTS PASSED ------")

    print("\nTESTING HOW MANY:\n")

    test_how_many(["a", "f", "d", "t"], ["a", "b", "c", "d", "e"])
    test_how_many(["a", "b", "f", "g", "a", "t", "c"], ["a", "b", "c", "d", "e"])
    test_how_many(["f", "g", "t"], ["a", "b", "c", "d", "e"])

    # MY TESTS
    # test_how_many([], ['a', 'b', 'c', 'd', 'e'])  # empty list1
    # test_how_many(['a', 'b', 'c'], [])  # empty list2
    # test_how_many([], [])  # both lists empty
    # test_how_many(['a', 'a', 'a'], ['a'])  # duplicates in list1
    # test_how_many(['a', 'b', 'c'], ['d', 'e', 'f'])  # no common elements
    # test_how_many(['a', 'b', 'c'], ['a', 'b', 'c'])  # all elements common
    # assert how_many([], ['a', 'b', 'c', 'd', 'e']) == 0
    # assert how_many(['a', 'b', 'c'], []) == 0
    # assert how_many([], []) == 0
    # assert how_many(['a', 'a', 'a'], ['a']) == 3
    # assert how_many(['a', 'b', 'c'], ['d', 'e', 'f']) == 0
    # assert how_many(['a', 'b', 'c'], ['a', 'b', 'c']) == 3
    # print("------ HOW_MANY TESTS PASSED ------")


if __name__ == "__main__":
    run_recursion_program()
