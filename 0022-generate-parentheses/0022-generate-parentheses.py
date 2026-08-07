class Solution:
    def generateParenthesis(self, n):
        result = []

        def backtrack(current, open_count, close_count):
            # A complete valid combination
            if open_count == n and close_count == n:
                result.append(current)
                return

            # Add '(' if available
            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)

            # Add ')' only when it won't make the string invalid
            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return result