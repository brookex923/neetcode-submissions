class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        neighbors = [[0,1], [1,0], [-1,0], [0,-1]]
        rows = len(heights)
        cols = len(heights[0])
        ans = []
        

        def bfs(i, j):
            seen = set()
            q = deque()
            q.append((i, j))
            pacific = False
            atlantic = False

            if i == 0 or j == 0:
                pacific = True
            if i == rows - 1 or j == cols - 1:
                atlantic = True
            seen.add((i, j))

            while q:
                x, y = q.popleft()
                for dx, dy in neighbors:
                    newx = x + dx
                    newy = y + dy
                    if 0<=newx<rows and 0<=newy<cols and heights[newx][newy] <= heights[x][y] and (newx, newy) not in seen:
                        seen.add((newx, newy))
                        q.append((newx,newy))
                        if newx == 0 or newy == 0:
                            pacific = True
                        if newx == rows - 1 or newy == cols - 1:
                            atlantic = True
            
            return [pacific, atlantic]
        
        for i in range(rows):
            for j in range(cols):
                bfs_array = bfs(i, j)
                p = bfs_array[0]
                a = bfs_array[1]
                if p and a:
                    ans.append([i, j])
        

        return ans



        