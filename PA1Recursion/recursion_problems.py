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
    #TODO: remove 'pass' and implement functionality
    # pass
    # print("lis1:    ", lis1)
    # print("list2:   ", lis2)

    # base case
    # if lis1 == lis2:
    #     return len(lis1)
    
    # if len(lis1) == 0 or len(lis2) == 0:
    #     return 0

    # # inductive step: check if lists have same first element
    # if lis1[0] == lis2[0]:
    #     return 1 + how_many(lis1[1:], lis2[1:])
    # else:
    #     return how_many(lis1, lis2[1:])
    

    # lis1.sort()
    # lis2.sort()

    if len(lis1) == 0 or len(lis2) == 0:
        return 0

    first = lis1[0]
    rest = lis1[1:]
    if first in lis2:
        return 1 + how_many(rest, lis2)
    else:
        return how_many(rest, lis2)


    # if lis1 > lis2:
    #     return how_many(lis1[:-1], lis2)

    # else: # len(lis1) < len(lis2)
    #     return how_many(lis1, lis2[:-1])



# FEEL FREE TO EDIT THE TESTS AND MAKE THEM BETTER
# REMEMBER EDGE CASES!

def test_modulus(num1, num2):
    print("The modulus of " + str(num1) + " and " + str(num2) + " is " + str(modulus(num1, num2)))

def test_how_many(lis1, lis2):
    print(str(how_many(lis1, lis2)) + " of the items in " + str(lis1) + " are also in " + str(lis2))

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

    assert modulus(8, 3) == 2
    assert modulus(9, 3) == 0
    assert modulus(10, 3) == 1
    assert modulus(11, 3) == 2
    assert modulus(8, 2) == 0
    assert modulus(0, 7) == 0
    assert modulus(15, 5) == 0
    assert modulus(128, 16) ==  0
    assert modulus(128, 15) ==  8
    # my tests
    assert modulus(1, 1) == 0
    assert modulus(1, 2) == 1
    assert modulus(2, 1) == 0
    assert modulus(15, 128) == 15
    print("------ MODULUS TESTS PASSED ------")

    print("\nTESTING HOW MANY:\n")

    test_how_many(['a', 'f', 'd', 't'], ['a', 'b', 'c', 'd', 'e'])
    test_how_many(['a', 'b', 'f', 'g', 'a', 't', 'c'], ['a', 'b', 'c', 'd', 'e'])
    test_how_many(['f', 'g', 't'], ['a', 'b', 'c', 'd', 'e'])


if __name__ == "__main__":
    run_recursion_program()