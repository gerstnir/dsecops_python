a = ()

b = (1,2,3)

c = ("Hello", "To", "All")

d = (1, "Hello", 0.52, False)

# # indexing

# d = (1, "Smart", 0.54, False)

# print(d)
# print(d[2])

# # tuple slicing
# print(d[0:2])
# print(d[0:])
# print(d[1:])
# print(d[:3])


# lists nested in tuples
ls1 = [1,2,3]
ls2 = [4,5,6]

ls3 = (ls1, ls2)

print( ls3[0][2])
print( ls3[1][1])

# # can't add new list to a tuple - it's immutable
# ls_new = [7,8,9]

# print(ls3)
# ls3.append(ls_new)
# print(ls3)

# tuples nested in lists
ls1 = (1,2,3)
ls2 = (4,5,6)

ls3 = [ls1, ls2]

# print( ls3[0][2])
# print( ls3[1][1])

# but i can add new tuple to a list - it IS mutable
t_new = (7,8,9)

print(ls3)
ls3.append(t_new)
print(ls3)