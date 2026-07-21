"""
Write a code that determines ticket_price(age)
takes an age from user and returns the price of a movie ticket based on these rules:
Under 5 years old: "Free"
From 5 to 17 years old: "$10"
From 18 to 64 years old: "$15"
65 years old and older: "$12"
"""
user_age=int(input("please enter your age"))
if user_age<5:
    print("You dont have to pay")
elif user_age>=5 and user_age<=17:
    print("Your ticket price is $10")
elif user_age >=18 and user_age<=64:
    print("Your ticket price is $15")
elif user_age >=65:
    print("Your Ticket price is $12")