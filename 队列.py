from collections import deque

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = deque(a)
b.append(11)
b.popleft()

print(f"{b}")
