class Solution:

    def encode(self, strs: List[str]) -> str:
        
        answer = ""
        for element in strs: 
            length = len(element)
            answer += str(length) + '#' + element
        return answer
    def decode(self, s: str) -> List[str]:
        intlist = [1,2,3,4,5,6,7,8,9,0]
        answer = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1 # j is delimiter char
            length = int(s[i:j])
            answer.append(s[j+1 : j + 1 + length])
            i = j+1+length #beginning of next string

                
        return answer
