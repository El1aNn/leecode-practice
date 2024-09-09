import random

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

random_key = random.choice(list(my_dict.keys()))
random_value = my_dict[random_key]

print(f"随机抽取的元素为：{random_key}: {random_value}")
