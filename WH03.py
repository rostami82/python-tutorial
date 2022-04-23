# d = int(input()) # 14
# f = int(input()) # 13
# s = int(input()) # 12

a = int(input()) # 14
b = int(input()) # 13
c = int(input()) # 12


# if d > s : 
#    d , s = s ,d 
# # d: 12, s: 14, f :13
# if d > f:
#     d, f = f, d
# if f > s:
#     f, s = s, f
# print(d, f, s) 

# if a < b < c:
#     print(a, "<", b, "<", c)
# elif a < c < b:
#     print(a, "<", C, "<", B)
# elif b < a < c:
#     print(b, "<", a, "<", c)
# elif b < c < a:
#     print(b, "<", c, "<", a)
# elif c < a < b:
#     print(c, "<", a, "<", b)
# elif c < b < a:
#     print(c, "<", b, "<", a)

min_num = a
mid_num = b 
max_num = c

if a < b < c:
    min_num = a
    mid_num = b
    max_num = c

elif a < c < b:
    min_num = a
    mid_num = c
    max_num = b

elif b < a < c:
    min_num = b
    mid_num = a
    max_num = c

elif b < c < a:
    min_num = b
    mid_num = c
    max_num = a

elif c < a < b:
    min_num = c
    mid_num = a
    max_num = b

elif c < b < a:
    min_num = c
    mid_num = b
    max_num = a



print(min_num, "<", mid_num, "<", max_num)