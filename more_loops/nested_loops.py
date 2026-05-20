# 1-10 integer product table (לוח הכפל)
# count = 0

# for x in range(1,11):
#     print("    x = ", x)
#     for y in range(1,11):
#         # print("x = ", x)
#         print("y = ", y, "hazara mispar", count)
#         count += 1
    
# print("number of hazarot: ", count)
#     # print("x * x = ",x*x)

for x in range(1,11):
    for y in range(1,11):
        # print(x,"*", y, "=" ,x*y)
        print(x*y, end=" ")
    print("")

# tirgul

for x in range(1,5):
    for y in range(1,5):
        print(x, ".", y)
