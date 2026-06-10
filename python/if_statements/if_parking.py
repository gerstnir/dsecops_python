up3 = 20
from3to5 = 15
from5to24 = 10
morethan24 = 5

total = 0

hours = int( input("How many hours did you park?: ") )

if hours >=0 and hours < 3 :
    total = hours * up3
elif hours >= 3 and hours < 5 :
    total = hours * from3to5
elif hours >= 5 and hours <= 24 :
    total = hours * from5to24
elif hours > 24 :
    total = hours * morethan24
else:
    print("Please enter a positive number !" )

print("\nYou need to pay", total, "NIS")