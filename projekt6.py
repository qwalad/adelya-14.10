lst = []
for i in range(10):
    lst.append(i)
    a = list(reversed(lst))
    sls_obj = slice(0 , 8)
    print(a[sls_obj])
