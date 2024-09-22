import random



dic = {1: -1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 1,
       13: -10, 14: -1, 15: -1, 16: -1, 17: -1, 18: -1, 19: -1, 20: -1, 21: -1, 22: -1, 23: -1}
ans = 0
n = 100000
for i in range(n):
    dic_f = dic.copy()
    red = 0
    blue = 0
    count = 0
    res = 10
    while count < 2:
        random_number = random.randint(1, 23)
        if random_number in dic_f:
            if abs(dic_f[random_number]) > 5:
                continue
            res += dic_f[random_number]
            del dic_f[random_number]
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
            random_number = random.randint(1, 23)
            if random_number in dic_f:
                if abs(dic_f[random_number]) > 5 and abs(res) > 5:
                    continue
                res += dic_f[random_number]
                del dic_f[random_number]
                count += 1
        if res < 0:
            red += 1
        else:
            blue += 1
    if abs(red - blue) > 3:
        ans += 1
print(red, blue)
print(ans / n)
