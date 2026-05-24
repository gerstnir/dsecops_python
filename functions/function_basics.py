# def func_name():
#     print("Hello world")

# func_name()

# # a function can separate assigning variables to two parts:
# # first part roughly means "x = "

# def f_name1 (x):
#     print(x)

# # second part roughly means " = 'shalom'"

# f_name('shalom')


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


# tirgul

def simple_function(name):
    print("Hello", name)

simple_function("ShemNafoz")


def prod_function(x,y):
    return x*y

prod_function(3,7)
print(prod_function(5,7))


def upto_function(x):
    for i in range(x):
        yield i

upto_20 = upto_function(20)

print(list(upto_20))