# boolean operators

A = True
B = False
C = True

print("A and B: ", A and B)
print("C or A: ", C or A)
print("not C: ", not C)
print("not A: ", not A)
print("not B: ", not B)

# boolean expressions

print(2 > 2 or 2 == 2)
print(2 > 2)
print(2 <= 2)

a = 5
b = 3
c = 2
d = 8
e = 3

# python's interperter runs "and" operators before "or" operators
print ((a>d) or (d>c) or (a>b) and (b==e) and (c!=d))


# float precision
a = 10
b = 4.5
c = 3

print( "a type: ", type(a), "b type: ", 
      type(b), "c type: ", type(c) )

print( a/b )
print( round(a/b, 4) )

print( a/c )
print( round(a/c, 5) )

print( c/b )
print( round(a/b, 2) )

print( a/b )
print(  round(a/b, 0) )


# showing round vs division to an integer
mish = round(9/3, 0)
print("mish: ", mish, "type: ", type(mish))

mish = 9//3
print("mish: ", mish, "type: ", type(mish))



# converting decimal number from user input to int can't be done directly
# and converting to float before converting to int is needed 
a = float( input("enter a number: ") ) 

a = int(a)

print("your number is", a)

# num = float( input("please enter a number: ") )

# print(num, type(num))

# showing that user input is string by default and no need for casting
num2_input =  input("please enter another number: ") 

# num2 = str(num2_input)

print(num2_input, type(num2_input))

input_str = input("enter a word: ")

input_len = len(input_str) # length of str

print( input_str, input_len )
print(type(input_len))