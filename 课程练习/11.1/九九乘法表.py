import xlwt
jiujiu = xlwt.Workbook(encoding="utf-8")
sheet = jiujiu.add_sheet("Sheet1")
for i in range(1, 10):
    for j in range(1, i+1):
        sheet.write(i-1, j-1, f"{i}*{j}={i*j}")
jiujiu.save("jiujiu.xls")
#print(f"{i}*{j}={i*j}\t", end='')
