# Write a Python program to find the sum of all numbers stored in a list.
list=[]
n=int(input("Enter the number"))
for i in range(n):
    list.append(i)
    sum=i+(i+1)
print(sum)
   