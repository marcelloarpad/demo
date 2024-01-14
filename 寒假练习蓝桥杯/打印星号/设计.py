row = int(input("需要打印的行数："))
n = row

print(" "*(n)+"/\\")
while n > 0:
    n -= 1
    xx = "*"*(row-(n))
    yy = " " * (n) + "/"
    dd = "\\"
    print(yy+xx+xx+dd)

a = row // 2
while a >= 0:
    a -= 1
    gg = "*" * (row // 2)
    cc = " " * (row // 2 + len(gg) // 2) + "|"
    print(cc + gg + "|")


