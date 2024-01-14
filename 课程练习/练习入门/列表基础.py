alist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, [1, 2, 3, 4, 5], 'nice', 'good']
print(len(alist))
print(alist[-1])
print(alist[-3][-1])#因为alist的-3位置上是一个列表，所以可以再次使用索引
print(alist[-1][2])#因为-1的位置上
print(alist[2:3])#切片从2开始到2结束
alist[10] = 'sss'
print(alist)
alist.append('dcjji')
print(alist)
alist.append([1, 2, 3, 3, 5, ['dffd']])
print(alist)