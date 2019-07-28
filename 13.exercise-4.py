# Create a function that return the largest number in the list

def get_largest_number(input):
    largest_number = input[0]
    for i in input:
        #print("i",i)
        if i > largest_number:
            largest_number = i
            #print("largest num",largest_number)
    return largest_number
    # largest = None

result = get_largest_number([1,2,3,4,5,12,1,6,99,2])
print(result) #99
