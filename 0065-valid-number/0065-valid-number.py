class Solution:
    def isNumber(self, s: str) -> bool:
        def isInteger(token: str) -> bool:
            if not token:
                return False
            if token[0] in ['+', '-']:
                token = token[1:]
            return token.isdigit()

        def isDecimal(token: str) -> bool:
            if not token:
                return False
            if token[0] in ['+', '-']:
                token = token[1:]
            if '.' not in token:
                return False
            left, right = token.split('.', 1)
            # At least one digit must exist
            if not left and not right:
                return False
            if left and not left.isdigit():
                return False
            if right and not right.isdigit():
                return False
            return True

        s = s.strip()
        if 'e' in s or 'E' in s:
            base, exp = s.lower().split('e', 1)
            return (isInteger(base) or isDecimal(base)) and isInteger(exp)
        else:
            return isInteger(s) or isDecimal(s)
