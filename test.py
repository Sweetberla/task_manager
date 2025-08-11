# program to calculate the average of two numbers

# take two numbers as input
user = int(input("put the first number\n"))
user1 =int(input("put the second number\n"))
# declare the average variable
average = (user + user1) /2
# declare average = (num1 + num2) / 2
# display the average
print(average)

#accept an age input from the user and a full name
age = int(input("enter your age\n"))
name =(input("enter your full name\n"))
#if the age is less than 18 and the average is equal to 20,
#print {name}, your are not allowed to vote
if age < 18 and int(average) == 20:
    print(f"{name} ,you are not allowed to vote")
# if the age is greater than or equal to 18 and the average is
# greater than or equal to 20 , print {name}, you are allowed to vote
elif age >= 18 and int(average) >= 20:
    print(f"{name}, you are allowed to vote")
    