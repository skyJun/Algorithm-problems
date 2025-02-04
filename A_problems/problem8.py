# 미생물 격리
# N by N개의 동일한 크기의 정사각형 셀
# 미생물들이 구역을 벗어나는 걸 방지하기 위해 가장 바깥쪽 가장자리 특수한 약품 있음

# 위치, 미생물 수, 이동 방향
# 1시간마다 이동방향에 있는 다음 셀로 이동
# 약품이 칠해진 셀로 도착하면 절반으로 죽고 이동방향 반대로 바뀜
# 미생물들이 한 셀에 모이는 경우 합쳐지고 이동방향은 가장 많은 군집의 이동방향
# M 시간 후 남아 있는 미생물의 총합을 구하라
import sys
from copy import deepcopy

sys.stdin = open('sample_input.txt', 'r')

# 방향 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def update_grid(grid: list):
    """
    시간마다 grid 업데이트 하는 함수
    """
    updated_grid = deepcopy(grid)
    moved_organ = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    for r_idx in range(len(grid)):
        for c_idx in range(len(grid[0])):
            if grid[r_idx][c_idx] is None:
                continue

            current_numbers, current_direction = grid[r_idx][c_idx]
            if not moved_organ[r_idx][c_idx]:
                # 일로 움직인 미생물이 있다면 정보 제거하면 안됨
                updated_grid[r_idx][c_idx] = None  # 정보 제거

            next_r_idx = r_idx + dr[current_direction]
            next_c_idx = c_idx + dc[current_direction]

            if updated_grid[next_r_idx][next_c_idx] and moved_organ[next_r_idx][next_c_idx]:
                # 업데이트하고자 하는 경우에 이미 값이 존재하는 경우 리스트 추가 추후에 정리
                # 이미 값이 옮겨져 있어야 함 만약 처음 간 곳이면 아님
                updated_grid[next_r_idx][next_c_idx].extend([current_numbers, current_direction])
                continue

            if next_r_idx == 0 or next_r_idx == (len(grid) - 1) or next_c_idx == 0 or next_c_idx == (len(grid[0]) - 1):
                # 가장자리에 도달하면
                next_numbers = current_numbers // 2
                if current_direction == 0:
                    next_direction = 1
                elif current_direction == 1:
                    next_direction = 0
                elif current_direction == 2:
                    next_direction = 3
                elif current_direction == 3:
                    next_direction = 2

                if next_numbers == 0:
                    # 업데이트하고자 하는 미생물 수가 없다면
                    continue
                updated_grid[next_r_idx][next_c_idx] = [next_numbers, next_direction]
                moved_organ[next_r_idx][next_c_idx] = True
            else:
                # 가장자리에 도달하지 않으면 진행
                updated_grid[next_r_idx][next_c_idx] = [current_numbers, current_direction]
                moved_organ[next_r_idx][next_c_idx] = True

    # 두 번째 반복문 중첩 되어 있는 거 정리하기
    for r_idx in range(len(grid)):
        for c_idx in range(len(grid[0])):
            if updated_grid[r_idx][c_idx] is None or len(updated_grid[r_idx][c_idx]) == 2:
                continue

            overwhelm_num = updated_grid[r_idx][c_idx][0]
            overwhelm_dir = updated_grid[r_idx][c_idx][1]
            total_numbers = sum(updated_grid[r_idx][c_idx][::2])

            for idx in range(2, len(updated_grid[r_idx][c_idx]), 2):
                if overwhelm_num > updated_grid[r_idx][c_idx][idx]:
                    continue

                overwhelm_num = updated_grid[r_idx][c_idx][idx]
                overwhelm_dir = updated_grid[r_idx][c_idx][idx + 1]

            updated_grid[r_idx][c_idx] = [total_numbers, overwhelm_dir]

    return updated_grid


T = int(input())
for t in range(1, T + 1):
    N, M, K = tuple(map(int, input().split()))

    grid_organ = [[None for _ in range(N)] for _ in range(N)]
    for _ in range(K):
        r_pos, c_pos, numbers, direction = tuple(map(int, input().split()))
        grid_organ[r_pos][c_pos] = [numbers, direction - 1]

    for _ in range(M):
        grid_organ = update_grid(grid_organ)

    result = sum(organ[0] for row in grid_organ for organ in row if organ is not None)
    # 리스트 컴프리헨션 쓸때 원래 for문 순서대로 유지해야함

    print(f'#{t} {result}')
