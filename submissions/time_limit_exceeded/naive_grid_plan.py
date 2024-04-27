import sys

def largestIsland(grid):
    N = len(grid)

    def neighbors(r, c):
        for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
            if 0 <= nr < N and 0 <= nc < N:
                yield nr, nc

    def dfs(r, c, visited):
        if (r, c) in visited or grid[r][c] == 0:
            return 0
        visited.add((r, c))
        ans = 1
        for nr, nc in neighbors(r, c):
            ans += dfs(nr, nc, visited)
        return ans

    answer = 0
    for r in range(N):
        for c in range(N):
            if grid[r][c] == 0:
                # Simulate building construction
                grid[r][c] = 1
                visited = set()
                new_area = dfs(r, c, visited)
                answer = max(answer, new_area)
                # Revert the simulation
                grid[r][c] = 0

    return answer

# Input handling
n = int(input())
grid = []
for i in range(n):
    grid.append(list(map(int, input().split())))

print(largestIsland(grid))
