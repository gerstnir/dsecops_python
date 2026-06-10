# a = input("Are you an Israeli citizen (Y/N)")

# if a == "Y":
#     b = int( input("Type your age: ") )
#     if b >= 18:
#         print("You deserve discount")
#     else:
#         print("You are too young for discount")

# else:
#     print("Only Israeli citizens can get discount")


# tirgul

is_toshav = input("Are you a Tel-Aviv resident? (Y/N) ")

if is_toshav == "Y":
    age = int( input("Type your age: ") )

    if age > 65:
        print("You deserve a discount")
    else:
        print("You are too young for discount")
    
else:
    print("Discount is for TLV residents only")