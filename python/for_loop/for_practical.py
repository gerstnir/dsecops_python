# email = input("Please type your email: ")

email = "goodemail@hotmail.com"
email2 = "bad.email@@hotmail.com"


count_at = 0
count_dot = 0

for x in email:
    if x == "@":
        # shorter form of count_at = count_at + 1
        count_at += 1
    elif x == "." :
        count_dot += 1

if count_at == 1 and count_dot == 1 :
    print("Email is OK")
else:
    print("Email not valid !")

