class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        no = []
        ans = []
        for i, x in enumerate(s):
            if x == '(' or x == ')':
                if x == '(':
                    stack.append(i)
                else:
                    if stack:
                        stack.pop()
                    else:
                        no.append(i)
        for i in range(len(s)):
            if i not in stack and i not in no:
                ans.append(s[i])
        return ''.join(ans)



s = Solution()
print(s.minRemoveToMakeValid("lee(t(c)o)de)"))  # "lee(t(c)o)de"
