l = [1, 2, 3]
p = l
p += [12]
a = "Hello World"
b = a
b += '2'
k = list(l)
k += [2]
l[0] = 5
k[0] += 1
p[0] += 3
print(k)
print(l)