class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #need bfs with distances

        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        queue = deque()

        
        
        neighbors = [[0,1], [1,0], [-1,0], [0,-1]]

        def addcell(i, j):
            if (i<0 or j<0 or i>=rows or j>=cols or grid[i][j] != 2147483647 
            or (i,j) in visited):
                return
            
            visited.add((i,j))
            queue.append([i,j])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    queue.append([i,j])
                    visited.add((i,j))

        dist = 0
        while queue:
            for i in range(len(queue)):
                x, y = queue.popleft()
                addcell(x+1, y)
                addcell(x, y+1)
                addcell(x-1, y)
                addcell(x, y-1)
                grid[x][y] = dist
            dist += 1
    

            


            