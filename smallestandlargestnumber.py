

# Develop a Python program to find the largest and smallest elements in a list.
str = input("Enter a list of numbers separated by spaces: ")

# Convert the input string to a list of numbers
list = [float(num) for num in str.split()]

# Check if the list is empty
if list:
    # Find the largest and smallest elements using built-in functions
    largest = max(list)
    smallest = min(list)

    # Print the largest and smallest elements
    print("The largest element in the list is: ",largest)
    print("The smallest element in the list is:", smallest)
else:
    print("The list is empty, no elements to compare.")