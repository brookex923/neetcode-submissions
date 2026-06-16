class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        for word in strs:
            added = False  # Flag to track if word was added to any group
            for group in output:
                if sorted(word) == sorted(group[0]):
                    group.append(word)
                    added = True
                    break
            if not added:  # If word didn't match any existing group
                output.append([word])
        return output
