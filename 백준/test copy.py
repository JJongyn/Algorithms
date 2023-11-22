class Solution:
    def uniquePathsIII(self, grid):
        m,n = len(grid), len(grid[0])
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    x,y = i,j
                if grid[i][j] == 0:
                    cnt += 1
        self.res = 0
        
        print(x,y,cnt)
        self.dfs(grid,x,y,cnt)
        return self.res
    
    def dfs(self,grid,x,y,cnt):
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == -1:
            return
        if grid[x][y] == 2:
            if cnt == -1:
                self.res += 1
            return
        grid[x][y] = -1
        self.dfs(grid,x+1,y,cnt-1)
        self.dfs(grid,x-1,y,cnt-1)
        self.dfs(grid,x,y+1,cnt-1)
        self.dfs(grid,x,y-1,cnt-1)
        grid[x][y] = 0
        
s = Solution()
print(s.uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,2,-1]]))