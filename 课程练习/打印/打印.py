with open("D:\\daima@\\dome\\打印\\poem.txt", "w", encoding= 'utf-8') as f:
    f.write("我欲乘风归去，\n")
    f.write("又恐琼楼玉宇，\n")
    f.write("高处不胜寒。")


'''with open(".\poem.txt", "r", encoding= 'utf-8') as f:
    qui = f.readlines()
    for quii in qui:
        print(quii)'''

with open(".\poem.txt", "a", encoding="utf-8" ) as f:
    f.write("\n 起舞弄清影，\n")
    f.write("何似在人间。\n")

with open(".\poem.txt", "r", encoding="utf-8") as f:
    s = f.readlines()
    for a in s:
        print(a)




