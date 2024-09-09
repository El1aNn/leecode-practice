# 集合{}，所有的元素都是唯一的
a = {1, 1.4, "asd"}
# 增加
a.add(1)
a.add(6)
a.update({3, 5, 6})
# 删除
a.remove(1)
print(a)
# 删除指定
a.discard(1.4)
a.discard("asd")
print(a)
# 集合做减法
b = {1, 3, 4}
c = a - b
print(c)
# 并集
c1 = a | b
# 交集
c2 = a & b
print(f"{c1}\n{c2}")
# 不同时有
c3 = a ^ b
print(f"{c3}\n")
m, n = 2, 3
dp = [[0] * (n + 1) for i in range(m + 1)]
print(dp)
print(10e6)