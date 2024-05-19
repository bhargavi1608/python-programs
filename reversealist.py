# Develop a Python program to reverse a given list.
n=input("Enter the numbers seperated by spaces : ").split()
original_list=[int(i) for i in n]
reversed_list=[]
length=len(original_list)
for i in range(length):
    reversed_list.append(original_list[length-1-i])
print("Original list: ",original_list)
print("revered list: ",reversed_list)