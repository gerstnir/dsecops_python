start = int( input( "enter a number to sum from (included in the sum):\n" ) )
stop = int( input( "enter a number to sum up to (not included in the sum):\n" ) )

numsum = 0

for x in range(start, stop):
    print("current sum is:", numsum, "Adding:", x)
    numsum += x

print("final sum is: ", numsum)