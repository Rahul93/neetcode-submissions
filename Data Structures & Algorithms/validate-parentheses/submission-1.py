class Solution:
    def isValid(self, s: str) -> bool:
        sc = deque()

        for ch in s:
            
            if sc:
                if ch == ')' or ch == '}' or ch == ']':
                    if ch == ')' and sc[-1] == '(':
                        sc.pop()
                    elif ch == ']' and sc[-1] == '[':
                        sc.pop()
                    elif ch == '}' and sc[-1] == '{':
                        sc.pop()
                    else:
                        sc.append(ch)
                else:
                    sc.append(ch)    
            else:
                sc.append(ch)

        return False if sc else True