'''Picnic Boat Ride Order
Five friends are enjoying a picnic outing. They are about to take a boat ride that only one
person can take at a time. After an argument about who should go first, they agree to
take the boat ride in alphabetical order of their names.
Write a program to take their names, each on one line, and print them back in sorted
order.
Example:
Input:anil
rahim
harita
babu
kapila
Output : anil
babu
harita
kapila
rahim'''

names=[]
n=int(input("Enter the number of friends"))
print("enter the friends names in line by line")
for i in range(n):
    name=input()
    names.append(name)
sorted_names=sorted(names)
print("Output: ")
for name in sorted_names:
    print(name)