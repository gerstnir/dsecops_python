# # basic for loop over a list
# c = ["Hi", "To", "All"]

# for x in c:
#     print(x)

# # example welcoming people to the course
# names = ["moshe", "shraga", "shirel"]

# for x in names:
#     print("Hello", x, "welcome to DevSecOps")

# c = [1, 3, 5]

# for x in range(5):
#     if x in c:
#     # equivalent to:
#     # if x == 1 or x == 3 or x == 5:
#         print(x)

# for x in range(5):
#     if x not in c:
      # equivalent to:
#     # if x != 1 and x != 3 and x != 5:
#         print(x)


# building list using a for loop and a range
# c = []

# for x in range(5):
#     c.append(x)
#     print(c)

# print(c)

# # list comprehension
# ls1 = ["Hi", "To", "All", "Of", "You"]
# ls2 = [ x for x in ls1 if "o" in x ]

# # # the above expression is equivalent to this:
# # ls2 = []
# # for x in ls1:
# #     if "o" in x:
# #         ls2.append(x)

# print(ls2)

# # copying lists
# ls1 = [ 1,3,5,7 ]
# # ls2 = ls1.copy()
# ls2 = list(ls1)

# print(ls2)

# # nested lists
# ls1 = [1,4,7]
# ls2 = [2,5,8]
# ls3 = [3,6,9]

# ls4 = [ ls1,ls2,ls3 ]

# print(ls1)
# print(ls2)
# print(ls3)

# # ls4 is a list
# print(ls4, type(ls4))

# # ls4 is a list, we use square brackets to reference into a list
# print(ls4[0], type(ls4[0]))

# # first element of ls4 is a list, again, we use square brackets to reference into a list
# # first element of the first element of ls4 is an int
# print(ls4[0][2], type(ls4[0][2]))

# tirgul

ls1 = [ x for x in range(101) ]
print(ls1)

ls2 = [ "alpha","bravo","charlie","delta","echo","foxtrot","golf","hotel","india","juliet" ]

for x in ls2:
    print(x)

ls3 = []

for x in ls2:
    if "a" in x:
        ls3.append(x)

print(ls3)


