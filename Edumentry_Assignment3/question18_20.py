"""
Question 18 - Display Variable Data Types
Create variables of different data types and display the datatype of each using the type() function.
Question 19 - Check Data Type
Create a variable named number with the value 50 and check whether it is an integer using the
isinstance() function.
Question 20 - Student Information Program
Write a Python program that takes a student's name, age, and favorite programming language as
input and displays all the information neatly
"""
#18
name=("Godsglory")
age=20
product=20.5
number1=2
print(type(name))
print(type(age))
print(type(product))
print(bool,number1)

#19
number=50
print(isinstance(number,int))

#20
student_name=input("please enter your full name")
age=input("please enter your age")
country=input("please enter your country")
favourite=input("please enter your favourite programming language")
print("Students name is : ",student_name)
print("students age is: ",age)
print("students country is: ",country)
print("students favourite programming language is: ",favourite)

