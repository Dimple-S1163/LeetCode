class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        prefix = ""

        for i in range(len(strs[0])):
            ch = strs[0][i]

            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[j][i] != ch:
                    return prefix

            prefix += ch

        return prefix