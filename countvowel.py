# Write a Python program to count the number of vowels in a string.
str=input("Enter the string")
Str=str.lower()
count=0
for i in Str:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        count+=1
if count==0:
    print("NO Vowel Found")
else:
    print("No.of Vowels Found= ",count)
    
