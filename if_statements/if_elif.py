# # slide 16

a = 5
b = -2

if a>0 and b>0:
    print("Both positive")
elif a>0 or b>0:
    print("One is positive")
elif a<0 and b<0:
    print("Both negative")
# only when one is negative and one is zero
elif a<0 or b<0: 
    print("One is negative")
# added in lecture
else:
    print("Both zero")

# slide 17

# a = input("Please enter a number between 1-5:\n")

# if a == "1":
#     print("one")
# elif a == "2":
#     print("two")
# elif a == "3":
#     print("three")
# elif a == "4":
#     print("four")
# elif a == "5":
#     print("five")
# else:
#     print("wrong number")

