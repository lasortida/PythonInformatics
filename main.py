# stri = "7" * 2022               # task № 1
# while "333" in stri or "777" in stri:
#     stri = stri.replace("777", "3", 1)
#     stri = stri.replace("333", "7", 1)
#
# print(stri)

# for i in range(-1000, 1000):  # task № 2
#     s = i
#     n = 200
#     while s > 0:
#         s //= 4
#         n -= 6
#     if n == 170:
#         print(i)
#         break

# def translate(a, ss):    # task № 3
#     string = ""
#     if (a > ss - 1):
#         string = translate(a // ss, ss) + string
#     return string + str(a % ss)
#
# a = 16 ** 23 + 4 ** 12 - 32 ** 6
# a = translate(a, 4)
# print(max([a.count("0"), a.count("1"), a.count("2"), a.count("3")]))

# for i in range(-1000, 1000):  # task № 4
#     x = i
#     L = 0
#     M = 0
#     while x > 0:
#         L += 1
#         if M < (x % 8):
#             M = x % 8
#         x //= 8
#     if (L == 4 and M == 7):
#         print(i)
#         break

def f(n, m):
    return (n % m == 0)


for A in range(1, 1000):
    OK = True
    for x in range(1, 1000):
        if int((not f(x, 54)) or (not f(x, 80))) <= int(not f(x, A)):
            OK *= True
        else:
            OK = False
            break
    if (OK):
        print(A)
        break



