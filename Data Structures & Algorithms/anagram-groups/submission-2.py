class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        diction = {str(sorted(strs[0])) : 0}
        ans = [[strs[0]]]
        for i in range(1, len(strs)):
            curr = str(sorted(strs[i]))
            if curr in diction.keys():
                ans[diction[curr]].append(strs[i])
            else:
                diction[curr] = len(ans)
                ans.append([strs[i]])
        
        return ans
        