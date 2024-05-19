# Simple Calculator: Create a program that takes two numbers from the user and
# performs addition, subtraction, multiplication, and division operations.
a=int(input("Enter the number 1 "))
b=int(input("Enter the number 2 "))
op=input()
if op=='+':
    print(a+b)
elif op=='-':
    print(a-b)
elif op=='*':
    print(a*b)
elif op=='/':
    print(a/b)
else:
    print("you entered incorrect operator")

