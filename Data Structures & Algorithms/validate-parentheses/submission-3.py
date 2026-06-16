class Solution:
    def isValid(self, s: str) -> bool:
        openqueue = []
        key = {')':'(', '}':'{', ']':'['}

        for c in s:
            
            if c in key.values():
                openqueue.append(c)
            else:
                if not openqueue:
                    return False
                popped = openqueue.pop()
                if popped != key[c]:
                    return False
        
        if len(openqueue) >0:
            return False
        
        return True

