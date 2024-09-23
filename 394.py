# 给定一个经过编码的字符串，返回它解码后的字符串。

# 编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。

# 你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。

# 此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。
# %%
class Solution:
    def decodeString(self, s: str) -> str:
        left, right = 0, 0
        ans = []
        num = []
        num_n = []
        index = []
        path = []
        for char in s:
            if char.isdigit():
                num_n.append(char)
                continue
            if char == '[':
                left += 1
                num.append(int(''.join(num_n)))
                num_n = []
                index.append(len(path))
                continue
            if char.isalpha():
                path.append(char)
            if char == ']':
                right += 1
                tmp = path[index[-1]:] * (num[-1] - 1) if num else []
                path.extend(tmp)
                num.pop()
                index.pop()
            if left == right:
                ans.extend(path.copy())
                path = []
        return "".join(ans)


s = Solution()
print(s.decodeString("10[a]"))
