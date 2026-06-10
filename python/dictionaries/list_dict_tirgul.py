# part 1 - two ways to get the index

first_names = ["fname1","fname2","fname3","fname4","fname5"]
full_names = {}

for fname in first_names:
    print("the name in the index is",
           fname, "and its index is:", 
           first_names.index(fname))

index = 0

for fname in first_names:
    print("the name in the index is",
        fname, "and its index is:",
        index)
index = index + 1

# part 2

first_names = ["moshe","shraga","aviv","yoav","fadi"]
full_names = {}

for x in first_names:
    print("the name in the index is",
           x, "and its index is:", 
           first_names.index(x))
    last_name = input("enter a last name for " + x + "\n")
    full_names[x] = last_name

print(full_names)