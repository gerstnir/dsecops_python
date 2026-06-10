a = "Smart"
b = a[0] + a[1] + "o" + a[3] + a[4]


print("a:", a)
print("b:", b)

# characters and indexes:
# a	b	c	d	e	f	g	h	i	j	k	l
# 0	1	2	3	4	5	6	7	8	9	10	11

st = "abcdefghijkl"

s0 = st[1] + st[8] + st[6] # big
s1 = st[10] + st[8] + st[3] # kid
s2 = st[2] + st[0] + st[10] + st[4] # cake
s3 = st[1] + st[0] + st[10] + st[4] # bake
s4 = st[6] + st[8] + st[6] + st[6] + st[11] + st[4] # giggle
print(s1, s2, s3, s4)