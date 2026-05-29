def func (name,age,city):
    # name =
    # age =
    # city =
    print("My name is: ", name)
    print("My age is: ", age)
    print("My city is: ", city)

func("nir", 99, "rehovot")
func(age=55,city="bat-yam",name="nir")
# func(age=25,city="Tel-aviv",name="moshe")

name = "shlomo"

# default values
def func2 (name,age=25,city="Tel-aviv"):
    # name =
    # age =
    # city =
    print("My name is: ", name)
    print("My age is: ", age)
    print("My city is: ", city)

func2("Moshe", 40,"Ramat gan")
# parameters inside the function that have a default values are not required as
# arguments when calling the function
func2("aviv")


# note that "name" inside the function and outside the function are two different variables
print(name)



# tirgul

## see func2 example above^

def func3(x,y=2.3333,z='goodbye'):

    print(x,y,z)

func3(3, 7.66671, 'hello')
func3(8)
