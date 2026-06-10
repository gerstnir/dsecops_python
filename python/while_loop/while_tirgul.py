# # original instructions from slides
# guess = 50
# number = int( input("Type a positive number: \n") )

# while number < guess or number < 0:
#     number = int( input("Try again!\nType a positive number: \n") )
#     print("not found")

# print("FOUND!")

# if we want to print found when number is between guess and 0

guess = 20
number = int( input("Type a positive number: \n") )

while number > guess or number <= 0:
    number = int( input("not found, try again!\nType a positive number: \n") )

print("FOUND!")
