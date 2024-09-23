# 设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。

# 实现 MinStack 类:

# MinStack() 初始化堆栈对象。
# void push(int val) 将元素val推入堆栈。
# void pop() 删除堆栈顶部的元素。
# int top() 获取堆栈顶部的元素。
# int getMin() 获取堆栈中的最小元素
# %%
class MinStack:

    def __init__(self):
        self.min_stack = []

    def push(self, val: int) -> None:

        if not self.min_stack:
            self.min_stack.append((val, val))
        else:
            self.min_stack.append((val, min(val, self.min_stack[-1][1])))

    def pop(self) -> None:
        if self.min_stack:
            self.min_stack.pop()

    def top(self) -> int:
        if self.min_stack:
            return self.min_stack[-1][0]

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1][1]

        # Your MinStack object will be instantiated and called as such:
        # obj = MinStack()
        # obj.push(val)
        # obj.pop()
        # param_3 = obj.top()
        # param_4 = obj.getMin()
s = MinStack()
s.push(-2)
s.push(-3)
