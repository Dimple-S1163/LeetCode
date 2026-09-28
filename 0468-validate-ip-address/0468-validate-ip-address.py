class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def isIPv4(ip: str) -> bool:
            parts = ip.split(".")
            if len(parts) != 4:
                return False
            for part in parts:
                if not part.isdigit():
                    return False
                if len(part) > 1 and part[0] == "0":
                    return False
                if not 0 <= int(part) <= 255:
                    return False
            return True

        def isIPv6(ip: str) -> bool:
            parts = ip.split(":")
            if len(parts) != 8:
                return False
            hex_digits = "0123456789abcdefABCDEF"
            for part in parts:
                if len(part) == 0 or len(part) > 4:
                    return False
                for ch in part:
                    if ch not in hex_digits:
                        return False
            return True

        if isIPv4(queryIP):
            return "IPv4"
        elif isIPv6(queryIP):   # ✅ properly closed parenthesis
            return "IPv6"
        else:
            return "Neither"
