class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        left = ['(', '[', '{']
        right = [')', ']', '}']
        for char in s:
            if char in left:
                stack.append(char)
            if char in right:
                if len(stack) != 0:
                    a = stack.pop()
                else:
                    return False
                if (a == '(' and char == ')') or (a == '[' and char == ']') or (a == '{' and char == '}'):
                    a = ''
                    continue
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False

    def isValid2(self, s: str) -> bool:
        dic = {'{': '}', '[': ']', '(': ')', '?': '?'}
        stack = ['?']
        for c in s:
            if c in dic:
                stack.append(c)
            elif dic[stack.pop()] != c:
                return False
        return len(stack) == 1


s = Solution()
print(s.isValid2("(){}[[()]]"))
