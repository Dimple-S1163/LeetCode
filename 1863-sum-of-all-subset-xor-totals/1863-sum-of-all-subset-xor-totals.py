class Solution:
    def subsetXORSum(self, nums):
        ans = 0

        def dfs(i, curr_xor):
            nonlocal ans

            if i == len(nums):
                ans += curr_xor
                return

            # Exclude current element
            dfs(i + 1, curr_xor)

            # Include current element
            dfs(i + 1, curr_xor ^ nums[i])

        dfs(0, 0)
        return ans