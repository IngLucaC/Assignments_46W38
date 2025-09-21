"""
MAX-MIN CODE (+SORT)
"""

# array initialization
array = []

# counter initialization
count=0

# while loop to create the array of numbers
while True:

    # update the counter
    count+=1
    x = input("Add a number or type 'end' to exit: ")
    
    if x == "end":
        # interrupt the loop if the user types 'end'
        if count==1:
            maxVar=None
            minVar=None
        break
    else:
        # convert the input from string to integer and save it into the vector names array, then print it
        array.append(int(x)) 
        print("Please enter a number or type 'end' to exit.")

# if the array is not empty, find the max and min
if array!=True and count>1:
    

    maxVar = array[0]
    minVar = array[0]

    # assign the elements of the array to the variable num one by one
    for num in array:
        if num > maxVar:
            maxVar = num
        if num < minVar:
            minVar = num

    print("The array is :", array)
    print("The maximum is :", maxVar)
    print("The minimum is :", minVar)

    # if the array is empty, then print max and min = None
else:
    print("The maximum is None")
    print("The minimum is None")

# sort
inputVar = int(input("Insert 1 for sorting in ascending order and 0 in descending order: "))

# set the variables a and b
#temp = [0]*len(array)

n = len(array)

# ascending order
for i in range(n):
    for j in range(i + 1, n):
        a = array[i]
        b = array[j]
        if a > b:
        
            # exchange the elements 
            if inputVar == 1:
                array[i], array[j] = b, a
        else:
            if inputVar == 0:
                array[i], array[j] = b, a
    
print("The array sorted is :", array)










        
        