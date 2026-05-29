# def func_name():
#     print("Hello world")

# func_name()

# # a function can separate assigning variables to two parts:
# # first part roughly means "x = "

# def f_name1 (x):
#     # x is the parameter
#     # x = 
#     # when we call the function, the arguement is the value that goes into x
#     # for example when we call f_name1(5) below, 5 is the argument that goes into the parameter x
#     print(x)

# # second part roughly means " = 'shalom'"

# f_name1(5) # here the argument is 5 (an integer)
# f_name1(11) # here the argument is 11

# f_name1('shalom') # here the argument is 'shalom' (a string)

# def f_name2 (x):
#     x = x + 1
#     print(x)

# # # equivalent to the following python code, 
# # # except x is replaced by what's in the parantheses ()
# # x = 3
# # x = x + 1
# # print(x)

# f_name2(3)

# f_name2(8)

# def f_name3(x,y):
#     # x = 
#     # y = 
#     if x > y:
#         print(x, "Is bigger than", y)
#     else:
#         print(y, "Is bigger than", x)

# f_name3(3,7)


# def f_name33(x):
#     # x = 
#     # using return means the function equals whatever is after "return"
#     # return 3 basically means f_name33() = 3
#     x = x + 10
#     # print(x)
#     return x

# # x = 5
# # x = x + 10
# # a = x

# a = f_name33(5)
# print(a)


# def f_name4 (x,y):
#     return (x*y)

# mish = f_name4(3,7)

# print(f_name4(3,7))

# def loopList1 (x):
#     for i in range(x):
#         return i
        
#     print("function finished")
    
# print( loopList1(5) )


# def loopList2 (x):
#     for i in range(x):
#         yield i
        
#     print("function finished")
    
# print( list(loopList2(5)) )

# # OPTIONAL - using recursive function
# def fact(x):
#     if x == 1:
#         return 1
#     else:
#         return (x * fact(x-1) )

# print( fact(5) )


# # tirgul

# def simple_function(name):
#     # name = 
#     print("Hello", name)

# simple_function("ShemNafoz")
# # name = "ShemNafoz"

# def prod_function(x,y):
#     # x = 
#     # y = 
#     return x*y

# prod_function(3,7)
# # print( prod_function(3,7) )
# print( prod_function(5,7) )


def upto_function(x):
    # adding x+1 to include x in the result
    for i in range(x+1):
        yield i

# for i in range(7+1):
#     print(i)

print( list( upto_function(7) ) )
print(list(upto_function(20)))


# ## OPTIONAL - recursive countdown ## this part is not mandatory!
# def recursive_countdown(x):
#     print(x)
#     # stopping condition
#     if x == 0:
#         return 0
#     # this part handles negative initial number as well
#     elif x < 0:
        
#         return recursive_countdown(x+1)
#     # the function takes a new argument which is the original argument minus 1
#     # print(x)
#     return recursive_countdown(x-1)

# recursive_countdown(10)
# recursive_countdown(-8)





