import hashlib
import matplotlib.pyplot as plt
import random
import numpy as np
from scipy import stats

# --------------------------------------------------------------------------------------------------- #

# to use my hash func
from MyHashableKey import MyHashableKey
# to generate random keys to test
import string
import math

# testing bucket distribution
from myTest import assess_bucket_distribution



"""
IMPORTANT! READ FIRST!
This script takes your hashfunction and tests it and plots the results to visualize how your hash performs.
This is not required and no extra points are given for using this.
You need to install three python packages, but before you do that it's recommended to create a virtual environment.
To create virtual environment execute `python3 -m venv env` in the terminal in your workspace. 
Then you have to source it with the command `source env/bin/activate`.
Now you are in a virtual environment and can install the packages with out them installing globally.
In the terminal run `pip3 install matplotlib numpy scipy` and now you should be able to run the code, given it's in the same workspace.

Note: remember to close the plot window for next run.
"""



m = hashlib.sha256()
length_of_list = 1000
amount_of_hashes = 1000000

def distribution_value(my_list):
    std = np.std(my_list)
    zscore = stats.zscore(my_list, axis=None)
    print(f"standard deviation: {std}")
    print(f"Z score is: {zscore}")
    print(f"Average zscore: {np.mean(zscore)}")
    

    return zscore # returning for testing purpose


def plotter(my_list):
    plt.plot(my_list)
    plt.ylim(bottom=0)
    plt.show()


def hakon_hasher():
    random_word = b""
    for _ in range(10):
        random_word += chr(random.randint(65, 122)).encode('ascii')
    hashed_string = hashlib.sha256(random_word).hexdigest()
    hashed_number = int(hashed_string, base=16)
    return hashed_number


def distribution():
    my_list = [0 for _ in range(length_of_list)]
    for i in range(amount_of_hashes):
        # you can import your function and replace this function call.
        # hashed_number = hakon_hasher()

        key = generate_random_key()
        hashed_number = hash(key)

        my_list[hashed_number % length_of_list] += 1
    return my_list


def generate_random_key():
    # Generate random integer (0-1000 as example)
    rand_int = random.randint(0, 1000)
    
    # Generate random string (length 10, ASCII letters + digits)
    rand_str = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    return MyHashableKey(rand_int, rand_str)


def display_statistics(my_list):
    """ Piazza TA statistics examples --- love that guy"""
        #  OUTPUT should be
        # staðalfrávik:     √(n * p * (1-p))
        # z score:          [-3 : 3]
        # average z score:    around 1,0000 (very close to 0)

        # calculate staðalfrávik
        # n = amount_of_hashes
        # p = 1 / length_of_list (1/1000).


    n = amount_of_hashes
    p = 1 / length_of_list
    std = math.sqrt(n * p * (1 - p))
    print("---------------------------")
    print("PERFECT Standar Deviation:")
    print(std)
    print("---------------------------\n")

    print("----- MY TESTS -----")
    difference = max(my_list) - min(my_list)
    print("Difference: ", difference)               # the lower the bettter
    print(f"Ratio: {difference / max(my_list)}")    # the closer to 0 the better (close to 1 is bad)
    print("---------------------\n")



if __name__ == "__main__":
    my_list = distribution() # get list

    display_statistics(my_list)    # my test

    # print(my_list)
    zscore = distribution_value(my_list)    # print result (standard deviation and z-score)

    assess_bucket_distribution(zscore)      # my test


    # plotter(my_list)               # set results up as graph




