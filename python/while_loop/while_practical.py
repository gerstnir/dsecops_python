# x = 10

# while x > 0:
#     print("*" * x, end="\n\n")
#     x = x - 1



# right_number = 84
# guess = int( input("Guess a number (1-100): ") )
# max_tries = 5
# curr_try = 0

# while guess != right_number and curr_try <= max_tries:
#     print("Wrong !")
#     guess = int( input("Guess again: ") )
#     curr_try = curr_try + 1

# if guess == right_number:
#     print("You are right !")
# else:
#     print("You lost")

summ = 0
amount = 0

print("Welcome to the shopping calculator!\n")
price = input('Type first price (or "stop" to exit): ')
# summ = summ + int(price)

while price != 'stop':
    # print("Current total sum is: ", summ)
    summ = summ + int(price)
    amount = amount + 1
    price = input('Type next price ("stop" to exit): ')
    # summ = summ + int(price)

print("\nThe total is: ", summ, "Nis\n")
print("\nThe product amount is: ", amount, "products\n")
print("\nThe average price is: ", round(summ/amount,2), "Nis\n")