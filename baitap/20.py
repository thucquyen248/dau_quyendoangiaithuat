class Solution:
    def isValid(self, s):
        stack = []
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        
        for ch in s:
            if ch in pairs.values():
                stack.append(ch)
            elif ch in pairs:
                top = stack[-1] if stack else None
                if top != pairs[ch]:
                    return False
                stack.pop()
            else:
                return False
        
        return len(stack) == 0