dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]
def inRange(r, c, N):
    return 0<= r < N and 0<=c <N

def dfs(r, c, N, adj_mine, visited):
    visited[r][c] = True
    if adj_mine[r][c] ==0:
        for dir in range(8):
            nr = r + dr[dir]
            nc = c + dc[dir]
            if inRange(nr, nc, N):
                if adj_mine[nr][nc] != -1 and not visited[nr][nc]:
                    dfs(nr, nc, N, adj_mine, visited)


T = int(input())

for t in range(1, T+1):
    N = int(input())
    board = []
    for _ in range(N):
        row = input()
        board.append(row)
    
    adj_mine = [[0 for _ in range(N)] for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if board[r][c] == '*':
                adj_mine[r][c] = -1
            else:
                mineCnt = 0
                for dir in range(8):
                    nr = r + dr[dir]
                    nc = c + dc[dir]
                    if inRange(nr, nc, N):
                        if board[nr][nc] == '*':
                            mineCnt += 1
                
                adj_mine[r][c] = mineCnt
    
    visited = [[False for _ in range(N)] for _ in range(N)]
    clicks = 0
    for r in range(N):
        for c in range(N):
            if adj_mine[r][c] == 0 and not visited[r][c]:
                clicks += 1
                dfs(r, c, N, adj_mine, visited)
    
    
    for r in range(N):
        for c in range(N):
            if adj_mine[r][c] != -1 and not visited[r][c]:
                clicks += 1
    
    
    print(f"#{t} {clicks}")