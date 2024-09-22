a = [1, 2, 5]
b = [1, 2, 3, 4, 5, 6]
# 查找
c = a[0]
# 增加
a.append(6)

# 改变
a[0] = 9
# 删除
d = a.pop(0)

# 常用函数
a0 = len(a)
a1 = max(a)
a2 = min(a)
a.reverse()  # 倒序
a.clear()  # 清空

# 遍历
a = [1, 2, 3, 4, 5]
# 1
for i in a:
    print(f"这是第{i}个")

# 2
for i in range(len(a)):
    print(f"这是第{a[i]}个")

# list comprehension

b = [i * i for i in a]

c = [i * i if i < 3 else i for i in a]
d = []
for i in range(len(a)):
    if a[i] < 3:
        d.append(a[i] * a[i])
    else:
        d.append(a[i])
a7 = [["1", "1", "1", "1", "0"],
      ["1", "1", "0", "1", "0"],
      ["1", "1", "0", "0", "0"],
      ["0", "0", "0", "0", "0"]]
print(len(a7))

print("好捏")
