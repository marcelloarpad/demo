n = 10
sum = 0
count = 0
print("please input 10 numbers:")
while count < n:
    number = float(input())
    sum = sum + number
    count = count + 1
average = sum / n
print("n = {}, sum = {}".format(n,sum))
print("Average = {:.2f}".format(average))
