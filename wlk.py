import numpy as np

# 定义参数
a1 = 0.5
b11 = 0.3
a2 = 0.7
b22 = 0.4
delta_t = 0.1

# 定义时间步长和空间步长
dt = delta_t
dx = 0.1  # 假设空间步长为0.1

# 定义空间网格
nx = 10
ny = 10

# 初始化R矩阵
R = np.zeros((nx, ny))


def chase_method(diag, upper, lower, b):
    n = len(diag)
    alpha = np.zeros(n)
    beta = np.zeros(n)
    x = np.zeros(n)

    # 分解
    alpha[0] = diag[0]
    for i in range(1, n):
        beta[i] = lower[i - 1] / alpha[i - 1]
        alpha[i] = diag[i] - beta[i] * upper[i - 1]

    # 前向替换
    y = np.zeros(n)
    y[0] = b[0]
    for i in range(1, n):
        y[i] = b[i] - beta[i] * y[i - 1]

    # 回代
    x[-1] = y[-1] / alpha[-1]
    for i in range(n - 2, -1, -1):
        x[i] = (y[i] - upper[i - 1] * x[i + 1]) / alpha[i]

    return x


# 示例用法
diag = np.array([1, 1, 1])
upper = np.array([0.5, 0.5])
lower = np.array([0.5, 0.5])
b = np.array([1, 2, 3])

solution = chase_method(diag, upper, lower, b)
print(solution)


# 迭代求解
def chase_method(diag, upper, lower, b):
    n = len(diag)
    alpha = np.zeros(n)
    beta = np.zeros(n)
    x = np.zeros(n)

    # 分解
    alpha[0] = diag[0]
    for i in range(1, n):
        beta[i] = lower[i - 1] / alpha[i - 1]
        alpha[i] = diag[i] - beta[i] * upper[i - 1]

    # 前向替换
    y = np.zeros(n)
    y[0] = b[0]
    for i in range(1, n):
        y[i] = b[i] - beta[i] * y[i - 1]

    # 回代
    x[-1] = y[-1] / alpha[-1]
    for i in range(n - 2, -1, -1):
        x[i] = (y[i] - upper[i - 1] * x[i + 1]) / alpha[i]

    return x


# 示例用法
diag = np.array([1, 1, 1])
upper = np.array([0.5, 0.5])
lower = np.array([0.5, 0.5])
b = np.array([1, 2, 3])

solution = chase_method(diag, upper, lower, b)
print(solution)
# 输出结果
print(R)
