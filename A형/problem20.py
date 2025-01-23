# 활주로 건설
# 각 셀의 숫자 지형의 높이
# 가로 또는 세로 방향 건설 가능성 확인
# 경사로의 길이 X 높이 1
# 경사로가 지형 밖을 넘어가면 안됨
# 시작 시간: 5시 35분, 종료 시간: 

def can_install(grid: list, row_idx: int, col_idx: int, X: int) -> bool:
    '''
    경사로 설치가능한지 여부 함수
    '''

    pass

T = int(input())
for t in range(1, T+1):
    N, X = map(int, input().split())
    count = 0

    grid = [[0 for _ in range(N)] for _ in range(N)]
    for idx in range(N):
        row = list(map(int, input().split()))
        grid[idx] = row
    
    for row_idx in range(N):
        start_height = grid[row_idx][col_idx]
        for col_idx in range(N):
            if start_height == grid[row_idx][col_idx]:
                continue
            else:
                if can_install(grid, row_idx, col_idx, X, True):
                    continue
                else:
                    break
        else:
            count += 1
    





    print(f'#{t} {count}')