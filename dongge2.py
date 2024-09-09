import random
import matplotlib.pyplot as plt
import numpy as np


def f(n):
    dic = {1: -1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 1,
           13: -10, 14: -1, 15: -1, 16: -1, 17: -1, 18: -1, 19: -1, 20: -1, 21: -1, 22: -1, 23: -1}
    ans = 0

    for i in range(n):
        dic_f = dic.copy()
        red = 0
        blue = 0
        count = 0
        res = 10
        while count < 2:
            random_key = random.choice(list(dic_f.keys()))
            random_value = dic_f[random_key]
            if abs(random_value) > 5:
                continue
            res += random_value
            del dic_f[random_key]
            count += 1
        if res < 0:
            red += 1
        else:
            blue += 1
        if abs(red - blue) > 3:
            ans += 1
        while dic_f:
            count = 0
            res = 0
            while count < 3:
                random_key = random.choice(list(dic_f.keys()))
                random_value = dic_f[random_key]
                res += random_value
                del dic_f[random_key]
                count += 1
            if res < 0:
                red += 1
            else:
                blue += 1
        if abs(red - blue) > 3:
            ans += 1
    return (ans / n)

print(f(10000000))
# n_values = range(1, 10001)
# f_values = [f(n) for n in n_values]
#
# # 绘制图像
# plt.plot(n_values, f_values)
# plt.xlabel('n')
# plt.ylabel('f(n)')
# plt.title('Function f(n) Graph')
# plt.show()
