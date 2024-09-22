from collections import deque


class RecentCounter:

    def __init__(self):
        self.Q = deque()

    def ping(self, t: int) -> int:
        self.Q.append(t)
        while self.Q[-1] - self.Q[0] > 3000:
            self.Q.popleft()

        return len(self.Q)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
