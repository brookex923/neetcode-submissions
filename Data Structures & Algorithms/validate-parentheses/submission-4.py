class Solution:
    def isValid(self, s: str) -> bool:
        openqueue = []
        key = {')':'(', '}':'{', ']':'['}

        for c in s:
            if c in key:
                if openqueue and openqueue[-1] == key[c]:
                    openqueue.pop()
                else:
                    return False
            else:
                openqueue.append(c)

        
        if len(openqueue) >0:
            return False
        
        return True

