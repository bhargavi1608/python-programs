# Develop a Python program to find the factorial of a number.
n=int(input("Enter the Number"))
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)

