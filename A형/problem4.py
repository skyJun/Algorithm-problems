# 디저트 카페
# 원 안의 숫자는 해당 디저트 카페에서 팔고 있는 디저트의 종류
# 카페들 사이에는 대각선 방향으로 움직일 수 있는 길
# 출발한 카페로 돌아와야 함
# 해당 지역을 벗어나면 안됨
# 카페 투어 중에 같은 숫자의 디저트를 팔고 있는 카페가 있으면 안됨
# 카페투어 하나만 가는 것도 안됨
# 왔던 길을 다시 돌아가는 것도 안됨
# 디저트를 가장 많이 먹을 수 있는 경로를 찾고, 그 때 디저트 수를 정답으로 출력하는 프로그램 작성
# 디저트를 먹을 수 없는 경우 -1을 출력

def in_range(x_idx: int,
             y_idx: int,
             range_n: int) -> bool:
    """
    Args:
        x_idx -- x coordinate
        y_idx -- y coordinate
        range_n -- Range of grid

    Returns:
        bool -- identify x and y in grid

    """
    return 0 <= x_idx < range_n and 0 <= y_idx < range_n


# 대각선 탐색 방향
# 우하단, 좌하단, 좌상단, 우상단
dx = [1, 1, -1, -1]
dy = [1, -1, -1, 1]


def dfs(cafe_grid: list, types: set, x_idx: int, y_idx: int, before_explore: int):
    """
    DFS 방식으로 탐색하여 디저트 투어 최대 가지수 반환하는 함수

    Args:
        cafe_grid -- 디저트 유형이 담겨 있는 좌표
        types -- 현재 투어했을 때 탐색한 디저트 유형들
        x_idx -- x 좌표
        y_idx -- y 좌표
        before_explore -- 전 노드에서 온 탐색 방향

    Returns:
        len(current_types) -- 탐색했을 때 최대 가짓수, 투어를 제대로 못했을 경우 -1 반환
    """

    for explore_type in range(4):
        next_x = x_idx + dx[explore_type]
        next_y = y_idx + dy[explore_type]
        if abs(explore_type - before_explore) == 2:
            # 바로 전 탐색 방향 노드로 돌아가면 이 탐색 방향은 스킵
            continue
        if in_range(next_x, next_y, len(cafe_grid)):
            # 다음 탐색이 범위 안에 있으면
            if cafe_grid[next_x][next_y] not in types:
                # 다음 디저트 유형이 투어에 없으면
                dfs(cafe_grid, types | {cafe_grid[next_x][next_y]}, next_x, next_y, explore_type)
        

    return -1


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    cafe = [[0 for _ in range(N)] for _ in range(N)]
    result = -1
    for idx in range(N):
        cafe[idx] = list(map(int, input().split()))

    for x in range(N):
        for y in range(N):
            start_x, start_y = x, y
            dessert_types = {cafe[start_x][start_y]}
            current_result = dfs(cafe, dessert_types, start_x, start_y, 0)
            if current_result > result:
                result = current_result

    print(f'#{t} {result}')
