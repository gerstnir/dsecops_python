# # using python variables - defining a variable again overwrites the original value
# name = "Elia Halevy"
# name = "Nir Eshet"
# course = "Python"
# age = 36

# print( name, course, age)

# # defining the same key in the dictionary 2 times, saves only the last definition
# student = { 
#     "name": "Elia Halevy",
#     "name": "Nir Eshet",
#     "course": "Python",
#     "age": 36
# }

# # calling a variable inside a dictionary
# student = { 
#     "name": "Elia Halevy",
#     "course": "Python",
#     "age": 36
# }
# print(student["course"])
# # print(student["name"], student["age"])

# student["course"] = "Java"

# print(student["course"])

# print(student)
# # # just like with regular python variables
# # course = "Python"
# # print(course)
# # course = "Java"
# # print(course)

# # adding new key-value pair
# student = {"name": "Elia Halevy",
#            "course": "Java",
#              "age": 36}

# print(student)

# student["status"] = "Active"

# print(student)

# # using pop
# student = {"name": "Elia Halevy",
#            "course": "Java",
#              "age": 36}

# print(student)

# student.pop("age")
# # # del works too
# # del student["age"]

# print(student)

# # get all keys in a dictionary
# student = {"name": "Elia Halevy",
#            "course": "Java",
#              "age": 36}

# print(student.keys())

# print(student.values())

# print(student.items())


# # # two methods to access the *values* of variables inside the dictionary
# # for x in student:
# #     # print(x)
# #     print(student[x])

# # for x in student.values():
# #     print(x)

# # # two methods to access the *keys* (or variables) inside the dictionary
# # for x in student:
# #     print(x)
# #     # print(student[x])

# # for x in student.keys():
# #     print(x)

# # getting both keys and values at the same time (key-value pairs)
# print(student.items())
# student["status"] = "Active"
# student["birthYear"] = "2005"
# print(student.items())

# for x,y in student.items():
#     print(x, y)

# # to get the tuples themselves inside student.items() use list()
# for x in list( student.items() ):
#     print( x, type(x) )

# tirgul

# my_dict = {"key1": "val1",
#            "key2": "val2",
#            "key3": 345

# }

# # equiavalent to:
# key1 = "val1"
# key2 = "val2"
# key3 = 678

# the vars inside the dictionary are separate from global variables
# print(key3, my_dict["key3"])

my_dict = {"key1": "val1",
           "key2": "val2",
           "key3": 345

}

print(my_dict.keys())
print(my_dict.values())

# example for list
my_list = ("val1", "val2", 345)
print(my_list[0])

#calling specific value by key name
print(my_dict["key1"])

for x,y in my_dict.items():
    print(x,y)

print(my_dict.items())