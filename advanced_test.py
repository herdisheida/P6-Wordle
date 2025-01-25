import array_list
from array_list import *
import sys
import shlex

class MyClass:
    def __init__(self, number, name, data):
        self.number = number
        self.name = name
        self.data = data

    def __str__(self):
        return "{" + self.name + " number " + str(self.number) + ": " + str(self.data) + "}"

def print_list(arr_lis):
    print("current list:", end = " ")
    print(arr_lis)

def get_as_correct_type(value, type):
    if type == 'string':
        return str(value)
    elif type == 'int':
        return int(value)
    elif type == 'my_class':
        values = value.split()
        return MyClass(int(values[0]), values[1], float(values[2]))
    else:
        return None


orig_stdout = sys.stdout
fout = open('out.txt', 'w+')
sys.stdout = fout

# f = open("tests.txt")
f = open(sys.path[0] + "/tests.txt")

type = None

for line in f:
    words = shlex.split(line)
    if len(words) == 0:
        continue
    else:
        print("\n    " + line.strip())
    if words[0] == "new":
        type = words[1]
        arr_lis = ArrayList()
        print_list(arr_lis)
    elif words[0] == "prepend":
        arr_lis.prepend(get_as_correct_type(words[1], type))
        print_list(arr_lis)
    elif words[0] == "append":
        arr_lis.append(get_as_correct_type(words[1], type))
        print_list(arr_lis)
    elif words[0] == "insert":
        try:
            arr_lis.insert(get_as_correct_type(words[1], type), int(words[2]))
            print_list(arr_lis)
        except IndexOutOfBounds:
            print("Index out of bounds!")
    elif words[0] == "set_at":
        try:
            arr_lis.set_at(get_as_correct_type(words[1], type), int(words[2]))
            print_list(arr_lis)
        except IndexOutOfBounds:
            print("Index out of bounds!")
    elif words[0] == "get_first":
        print_list(arr_lis)
        try:
            print("value: " + str(arr_lis.get_first()))
        except Empty:
            print("The list is empty!")
        except IndexOutOfBounds:
            print("Index out of bounds!")
    elif words[0] == "get_at":
        print_list(arr_lis)
        try:
            print("value: " + str(arr_lis.get_at(int(words[1]))))
        except IndexOutOfBounds:
            print("Index out of bounds!")
    elif words[0] == "get_last":
        print_list(arr_lis)
        try:
            print("value: " + str(arr_lis.get_last()))
        except Empty:
            print("The list is empty!")
        except IndexOutOfBounds:
            print("Index out of bounds!")
    elif words[0] == "remove_at":
        try:
            arr_lis.remove_at(int(words[1]))
            print_list(arr_lis)
        except IndexOutOfBounds:
            print("Index out of bounds!")
    elif words[0] == "clear":
        arr_lis.clear()
        print_list(arr_lis)
    elif words[0] == "insert_ordered":
        try:
            arr_lis.insert_ordered(get_as_correct_type(words[1], type))
            print_list(arr_lis)
        except NotOrdered:
            print("The list is not ordered")
    elif words[0] == "find":
        print_list(arr_lis)
        try:
            index = arr_lis.find(get_as_correct_type(words[1], type))
            print("index of value: " + str(index) + " | value at index: " + str(arr_lis.get_at(index)))
        except NotFound:
            print("Value not found in list")
    elif words[0] == "remove_value":
        try:
            arr_lis.remove_value(get_as_correct_type(words[1], type))
            print_list(arr_lis)
        except NotFound:
            print("Value not found in list")

f.close()

sys.stdout = orig_stdout
fout.close()

def run_test_script(test_file, expected_output_file):
    arr_lis = ArrayList()
    with open(test_file, 'r') as f, open(expected_output_file, 'r') as expected_f:
        test_lines = f.readlines()
        expected_lines = expected_f.readlines()
        output = []
        for line in test_lines:
            parts = line.strip().split()
            command = parts[0]
            args = parts[1:]
            try:
                if command == "new":
                    arr_lis = ArrayList()
                elif command == "prepend":
                    arr_lis.prepend(eval(args[0]))
                elif command == "append":
                    arr_lis.append(eval(args[0]))
                elif command == "insert":
                    arr_lis.insert(eval(args[0]), int(args[1]))
                elif command == "set_at":
                    arr_lis.set_at(eval(args[0]), int(args[1]))
                elif command == "get_first":
                    output.append(f"value: {arr_lis.get_first()}")
                elif command == "get_at":
                    output.append(f"value: {arr_lis.get_at(int(args[0]))}")
                elif command == "get_last":
                    output.append(f"value: {arr_lis.get_last()}")
                elif command == "remove_at":
                    arr_lis.remove_at(int(args[0]))
                elif command == "clear":
                    arr_lis.clear()
                elif command == "insert_ordered":
                    arr_lis.insert_ordered(eval(args[0]))
                elif command == "find":
                    index = arr_lis.find(eval(args[0]))
                    output.append(f"index of value: {index} | value at index: {arr_lis.get_at(index)}")
                elif command == "remove_value":
                    arr_lis.remove_value(eval(args[0]))
                output.append(f"current list: {str(arr_lis)}")
            except (IndexOutOfBounds, Empty, NotOrdered, NotFound) as e:
                output.append(str(e))
        
        with open("out.txt", "w") as out_f:
            out_f.write("\n".join(output))
        
        with open("out_diff.txt", "w") as diff_f:
            for i, (out_line, exp_line) in enumerate(zip(output, expected_lines)):
                if out_line.strip() != exp_line.strip():
                    diff_f.write(f"Difference in line {i + 1}\n")

if __name__ == "__main__":
    run_test_script("tests.txt", "expected_out.txt")
    run_test_script("extra_tests.txt", "extra_expected_out.txt")
