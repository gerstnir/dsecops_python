up3 = 20
from3to5 = 15
from5to24 = 10
morethan24 = 5

total = 0

hours = int( input("How many hours did you park?: ") )


if hours >= 0 and hours < 3 :
    total = hours * up3 # 1 - 0.15
elif hours >= 3 and hours < 5 :
    total = hours * from3to5
elif hours >= 5 and hours < 24 :
    total = hours * from5to24
elif hours > 24:
    total = hours * morethan24
else:
    print("Please enter a positive number !")


member = input("Do you have a manui? (Y/N)\n")

if member == "Y" or member == "yes" or member == "y" or member == "YES":
    memberDiscount = 10 # percent %
    total = total * (100 - memberDiscount )/100
else:
    memberDiscount = 10 # percent %
    total = total * (100 - memberDiscount )/100

    age = int( input("Type your age: ") )

    if age >= 18 and age < 30:
        total = total + 100
    elif age >= 30 and age < 60:
        total = total + 80
    elif age > 60:
        total = total + 50

print("\nYou need to pay", total, "NIS")