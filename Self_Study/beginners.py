# Beginner Exercises
# 1. Number Printer: Print numbers from 1 to 10.
# 2. Even Finder: Print only the even numbers between 1 and 20.
# 3. Sum Accumulator: Calculate and print the sum of all numbers from 1 to 50.
# 4. List Multiplier: Multiply every number in the list [2, 4, 6, 8] by 3 and print the results.
# 5. Character Counter: Loop through the string "Python" and print each letter on a new line.

# for i in range(1,11):
#     print (i)

# for i in range(1,21):
#     if i%2==0:
#         print(i)
# #OR
# for i in range(2,21,2):
#     print(i)

# sum=0
# for i in range(1,51):
#     sum+=i
#     print("The sum is",sum)

numbers = [2, 4, 6, 8]
for num in numbers:
    result = num * 3
    print(result)