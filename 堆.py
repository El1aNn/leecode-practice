from heapq import heapify, heappop, heappush, nlargest, nsmallest

a = [1, 2, 3, 4]
heapify(a)
heappush(a, 5)
print(a)
b = heappop(a)
print(b)
print(a)
c = nlargest(2, a)
print(c)
d = nsmallest(2, a)
print(d)
