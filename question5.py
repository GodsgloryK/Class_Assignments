"""
Assignment 5: Simple Calculator
Write a Python program that:

Takes two numbers as input from the user.
Converts both inputs into integers.
Calculates and displays:
Sum
Difference
Product
Quotient
"""
num1=input("please input the first number")
number1=int(num1)
num2=input("please input the second number")
number2=int(num2)

sum=number1+number2
diff=number1-number2
product=number1*number2
quotient=number1//number2

print("the sum is",sum,sep=":")
print("the difference is",diff,sep=":")
print("the product is",product,sep=":")
print("the quotient is",quotient,sep=":")
