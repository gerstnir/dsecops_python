up3 = 20
from3to5 = 15
from5to24 = 10
morethan24 = 5

total = 0

hours = int( input("How many hours did you park?: ") )

member = input("Do you have a manui? (Y/N)\n")

if member == "Y" or member == "yes" or member == "y" or member == "YES":
    memberDiscount = 0.15
else:
    memberDiscount = 0

if hours >= 0 and hours < 3 :
    total = hours * up3 * (1 - memberDiscount ) # 1 - 0.15
elif hours >= 3 and hours < 5 :
    total = hours * from3to5 * (1 - memberDiscount )
elif hours >= 5 and hours < 24 :
    total = hours * from5to24 * (1 - memberDiscount )
elif hours > 24:
    total = hours * morethan24 * (1 - memberDiscount )
else:
    print("Please enter a positive number !")


# if member == "Y":
#     total = total * 0.9

print("\nYou need to pay", total, "NIS")