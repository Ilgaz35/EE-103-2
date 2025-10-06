import random

def check_type(number):
    return type(number)

range_num = range(int(input("Enter a range:")))
user_wish = input("Do you want to learn type:").upper()


if user_wish == "Y":
    number = random.choice(range_num)
    print(f"Number: {number}")
    print(f"Type: {check_type(number)}")
else:
    print("okay")
    