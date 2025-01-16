T = int(input())
#90도 180도 270도 각각 열에 해당함
for t in range(1, T+1):
    print(f"#{t}")
    N = int(input())
    grid = [[0 for _ in range(N)] for _ in range(N)]
    
    for i in range(N):
        row = list(input().split())
        grid[i] = row
    
    
    for c in range(N):
        index_90 = ""
        index_180 = ""
        index_270 = ""
        for j in range(N):
            index_90 += grid[N-1 - j][0 + c]
            index_180 += grid[N-1 - c][N-1 - j]
            index_270 += grid[0 + j][N-1 - c]
        
        print(f"{index_90} {index_180} {index_270}")

