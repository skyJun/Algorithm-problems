T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    grid = [[-1 for _ in range(N)] for _ in range(N)]
    
    for i in range(N):
        grid[i] = list(map(int, input().split()))
    
    max_flies = 0
    
    for r in range(N):
        for c in range(N):
            sum_plus = grid[r][c]
            for step in range(1, M):
                nr_up = r - step
                if nr_up >=0:
                    sum_plus += grid[nr_up][c]
                nr_down = r + step
                if nr_down < N:
                    sum_plus += grid[nr_down][c]
                
                nc_left = c - step
                if nc_left >= 0:
                    sum_plus += grid[r][nc_left]
                nc_right = c + step
                if nc_right < N:
                    sum_plus += grid[r][nc_right]
            
            
            sum_x = grid[r][c]
            for step in range(1, M):
                nr_lu = r - step
                nc_lu = c - step
                if nr_lu >= 0 and nc_lu >=0:
                    sum_x += grid[nr_lu][nc_lu]
                
                nr_ld = r + step
                nc_ld = c - step
                if nr_ld < N and nc_ld >=0:
                    sum_x += grid[nr_ld][nc_ld]
                
                nr_ru = r - step
                nc_ru = c + step
                if nr_ru >= 0 and nc_ru < N:
                    sum_x += grid[nr_ru][nc_ru]
                
                nr_rd = r + step
                nc_rd = c + step
                if nr_rd < N and nc_rd < N:
                    sum_x += grid[nr_rd][nc_rd]
            
            max_flies = max(max_flies, sum_plus, sum_x)
    print(f"#{t} {max_flies}")