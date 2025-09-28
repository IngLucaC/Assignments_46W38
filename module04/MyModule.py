# MyModule.py


def get_a_list_of_numbers():

    # array initialization
    array = []

    # while loop to create the array of numbers
    while True:

        x = input("Add a number or type 'end' to exit: ")

        if x == "end":
            # interrupt the loop if the user types 'end'
            break
        try:
            # convert the input from string to integer and save it into the vector names array, then print it
            array.append(int(x))
            print("Please enter a number or type 'end' to exit.")
        except ValueError:
            print("Invalid input. Please enter a valid number or type 'end' to exit.")
    return array


def find_min(array):

    # if the array is not empty, find the min
    if not array:
        minVar = None
    else:
        minVar = min(array)
    return minVar


def find_max(array):

    # if the array is not empty, find the max
    if not array:
        maxVar = None
    else:
        maxVar = max(array)
    return maxVar
