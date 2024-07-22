# DFS-2

## Problem1 (https://leetcode.com/problems/number-of-islands/)

#BFS solution
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        direction = ((1,0),(0,1),(0,-1),(-1,0))
        visited = set()
        count = 0
        q = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i,j) not in visited:
                    count += 1
                    q.append([i,j])
                    visited.add((i,j))
        
                    while q: 
                        r,c = q.popleft()
                        for dr,dc in direction:
                            nr = r + dr
                            nc = c + dc

                            if nr >= 0 and nc >= 0 and nr < m and nc < n and grid[nr][nc] == '1' and (nr, nc) not in visited:
                                q.append([nr,nc])
                                grid[nr][nc] = 0
                                

        return count


#DFS solution

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid and grid[0]:
            return 0
        
        islands = 0
        visited = set()
        row, col = len(grid), len(grid[0])

        def dfs(r,c):
            if (
                r not in range(row) 
                or c not in range(col) 
                or grid[r][c] == "0" 
                or (r,c) in visited
                ):
                return

            visited.add((r,c))
            directions = [[0,1], [0,-1], [1,0], [-1,0]]
            for dr,dc in directions:
                dfs(r+dr, c+dc)

        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1" and (r,c) not in visited:
                    islands += 1
                    dfs(r,c)

        return islands