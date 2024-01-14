def f(a, data = None):
    if data is None:
        data = []
    data.append(a)
    return data

while True:
    a = input()
    result_data = f(a)
    print(result_data)

#默认参数None是不可变参数，与1不tong