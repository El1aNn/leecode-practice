# 元组 ：无法修改 只能查
a = (1, 2, 3, 4, "abc")
print(f"{3 in a}")

b = a[0:3]
print(f"{4 in b}")
c = (50)
print(type(c))
c = (50,)
print(type(c))
