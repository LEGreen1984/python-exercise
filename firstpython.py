import datetime
print("hello world!")
age = input("what is your age?")
century = int(2020 - age) + 100
print("you will be 100 years old in the year {0}").format(century)

number = input("enter a number")
if int(number) % 2 == 0:
    print("you have an even number")
else:
    print("we have an odd number")
