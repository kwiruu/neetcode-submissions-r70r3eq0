class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) % 2 != 0:
            return False

        for i in range(len(s)):
            match s[i]:
                case '(':
                    stack.append('(')
                case '[':
                    stack.append('[')
                case '{':
                    stack.append('{')
                case ')':
                    if stack and stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
                case ']':
                    if stack and stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
                case '}':
                    if stack and stack[-1] == '{':
                        stack.pop()
                    else:
                        return False
        if len(stack) == 0:
            return True
        else:
            return False