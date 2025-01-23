# 활주로 건설
# 각 셀의 숫자 지형의 높이
# 가로 또는 세로 방향 건설 가능성 확인
# 경사로의 길이 X 높이 1
# 경사로가 지형 밖을 넘어가면 안됨
# 시작 시간: 5시 35분, 종료 시간:  총 걸린 시간 1시간 30분 정도

def can_install(grid: list, installed: list, row_idx: int, col_idx: int, X: int, row: bool) -> bool:
    '''
    경사로 설치가능한지 여부 함수
    '''
    current_height = grid[row_idx][col_idx]

    if not row:
        start_height = grid[row_idx - 1][col_idx]
        if start_height > current_height:
            # 경사로를 인덱스가 증가하는 방향으로 설치
            if row_idx + X <= N:
                # 설치 가능 1조건
                for idx in range(row_idx, row_idx + X):
                    next_height = grid[idx][col_idx]
                    if next_height != current_height:
                        # 설치 불가능
                        return False
                    if installed[idx][col_idx]:
                        return False
                
                # 설치 가능
                for idx in range(row_idx, row_idx + X):
                    installed[idx][col_idx] = True
                
            else:
                return False
        else:
            # 경사로를 인덱스가 감소하는 방향으로 설치
            if row_idx - X >= 0:
                # 설치 가능 1조건
                for idx in range(row_idx - 1, row_idx - X - 1, -1):
                    next_height = grid[idx][col_idx]
                    if next_height != (current_height - 1):
                        # 설치 불가능
                        return False
                    if installed[idx][col_idx]:
                        return False

                # 설치 가능
                for idx in range(row_idx - 1, row_idx - X - 1, -1):
                    installed[idx][col_idx] = True
                
            else:
                return False
    else:
        # 가로 방향 검사
        start_height = grid[row_idx][col_idx - 1]
        if start_height > current_height:
            # 경사로를 인덱스가 증가하는 방향으로 설치
            if col_idx + X <= N:
                # 설치 가능 1조건
                for idx in range(col_idx, col_idx + X):
                    next_height = grid[row_idx][idx]
                    if next_height != current_height:
                        # 설치 불가능
                        return False
                    if installed[row_idx][idx]:
                        return False
                
                # 설치 가능
                for idx in range(col_idx, col_idx + X):
                    installed[row_idx][idx] = True
                
            else:
                return False
        else:
            # 경사로를 인덱스가 감소하는 방향으로 설치
            if col_idx - X >= 0:
                # 설치 가능 1조건
                for idx in range(col_idx - 1, col_idx - X - 1, -1):
                    next_height = grid[row_idx][idx]
                    if next_height != (current_height - 1):
                        # 설치 불가능
                        return False
                    if installed[row_idx][idx]:
                        return False
                
                # 설치 가능
                for idx in range(col_idx - 1, col_idx - X - 1, -1):
                    installed[row_idx][idx] = True
            else:
                return False
    
    return True

T = int(input())
for t in range(1, T+1):
    N, X = map(int, input().split())
    count = 0

    grid = [[0 for _ in range(N)] for _ in range(N)]
    for idx in range(N):
        row = list(map(int, input().split()))
        grid[idx] = row
    
    for row_idx in range(N):
        start_height = grid[row_idx][0]
        installed = [[False for _ in range(N)] for _ in range(N)]
        can_build = True
        for col_idx in range(N):
            if start_height == grid[row_idx][col_idx]:
                continue
            elif abs(start_height - grid[row_idx][col_idx]) == 1:
                if can_install(grid, installed, row_idx, col_idx, X, True):
                    start_height = grid[row_idx][col_idx]
                    continue
                else:
                    can_build = False
                    break
            else:
                can_build = False
                break
        
        if can_build:
            count += 1
    
    for col_idx in range(N):
        start_height = grid[0][col_idx]
        installed = [[False for _ in range(N)] for _ in range(N)]
        can_build = True
        for row_idx in range(N):
            if start_height == grid[row_idx][col_idx]:
                continue
            elif abs(start_height - grid[row_idx][col_idx]) == 1:
                if can_install(grid, installed, row_idx, col_idx, X, False):
                    start_height = grid[row_idx][col_idx]
                    continue
                else:
                    can_build = False
                    break
            else:
                can_build = False
                break
        
        if can_build:
            count += 1

    print(f'#{t} {count}')