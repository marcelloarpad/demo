'''def jie_cheng(num):
    if num ==0:
        return 1
    return num * jie_cheng(num-1)
num =int(input())
print(jie_cheng(num))

def jie_cheng2(number):
    result = 1
    while number>0:
        result*=number
        result-=1
    return result

print(jie_cheng2(8))

'''
def jiecheng(number):
    result = 1
    while number>0:
        result*=number
        number-=1
    return result

print(jiecheng(6))
