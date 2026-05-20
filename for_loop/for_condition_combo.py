# for x in range(100):
#     if x % 2 == 0:
#         print(x, "Is Even")
#     else:
#         print(x, "Is Odd")

# if a variable is even (זוגי) we get x % 2 == 0 and if it's odd (אי זוגי) we get x % 2 == 1
# x = 6

# bool_var = x % 2
# print(bool_var)
# print(bool(bool_var))


# sum_evens = 0
# sum_odds = 0

# for x in range(1000, 5000):
#     print(x)
#     if x % 2 == 0:
#         sum_evens = sum_evens + x
#     else:
#         sum_odds = sum_odds + x

# print("Total sum of evens: ", sum_evens)
# print("Total sum of odds: ", sum_odds)

# # if x is a vowel print it
# string = "aejfhbskjhcebewwvdopincxv"

# for x in string:
#     if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
#         print(x)

# # count number of times letter e appears in string
# string = "aejfhbskjhcebewwvdopincxv"

# count = 0

# for x in string:
#     if x == "e":
#         count = count + 1

# print(count)

# tirgul


# # sum numbers that can be divided by 3
# sum_div3 = 0

# for x in range(1000, 5000):
#     print(x)
#     if x % 3 == 0:
#         print("added", x, "to sum")
#         sum_div3 = sum_div3 + x

# print("Total sum of divisable by 3: ", sum_div3)

# count number of a in string
string = input("enter a string: ")

a_count = 0

for x in string:
    if x == "a":
        a_count = a_count + 1

print(a_count)