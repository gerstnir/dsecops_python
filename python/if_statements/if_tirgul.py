# age = int( input("Please enter your age in years: ") )

# if age > 18:
#     print("ata yakhol lehikanes")
# else:
#     print("you are too tzaeer")


up3 = 20
over3 = 10

total = 0

hours = int( input("How many hours did you park?: ") )

if hours >= 0 and hours <= 3 :
    total = hours * up3
elif hours > 3  :
    total = hours * over3
else:
    print("Please enter a positive number !" )

print("\nYou need to pay", total, "NIS")