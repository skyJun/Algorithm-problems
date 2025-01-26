# 원자 소멸 시뮬레이션
# 원자가 충돌 할 경우 충돌한 원자들은 각자 보유한 에너지를 모두 방출하고 소멸

# 원자의 움직임
# 1. 원자의 최초 위치는 2차원 평면상의 [x, y]
# 2. 원자는 각자 고유의 움직이는 방향을 가지고 있음 상 하 좌 우
# 3. 모든 원자들의 이동속도 동일 1만큼 이동
# 4. 모든 원자들은 최초 위치에서 동시에 이동 시작
# 5. 충돌한 원자들은 모두 보유한 에너지를 방출하고 소멸

# 원자들의 보유 에너지가 다 다름
# 1초에 1씩 거리를 이동하는데 지금 보니 두 원자 사이 거리의 평균으로 계산하네
# 동시에 2개 이상의 원자들이 충돌하면 이 에너지를 다 합
# 구하고자 하는 목표 원자들이 소멸되면서 방출하는 에너지의 총합

# 상 하 좌 우 0 1 2 3
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def find_min_distance(idx: int, atoms: list) -> tuple[float, int]:
    start_x, start_y, direction, _ = atoms[idx]
    min_distance = 0
    if direction == 0:
        # 상
        candidates_atoms = [(atom, idx) for idx, atom in enumerate(atoms) if (atom[1] > atoms[idx][1]) and (atom[0] == atoms[idx][0]) and (atom[2] == 1)]
    elif direction == 1:
        # 하
        candidates_atoms = [(atom, idx) for idx, atom in enumerate(atoms) if (atom[1] < atoms[idx][1]) and atom[0] == atoms[idx][0] and (atom[2] == 0)]
    elif direction == 2:
        # 좌
        candidates_atoms = [(atom, idx) for idx, atom in enumerate(atoms) if (atom[0] > atoms[idx][0]) and atom[1] == atoms[idx][1] and (atom[2] == 3)]
    elif direction == 3:
        # 우
        candidates_atoms = [(atom, idx) for idx, atom in enumerate(atoms) if (atom[0] < atoms[idx][0]) and atom[1] == atoms[idx][1] and (atom[2] == 2)]

    

T = int(input())
for t in range(1, T+1):
    N = int(input())
    atoms = [] # 원자 정보 (x, y, 이동방향, 에너지)
    for _ in range(N):
        atoms.append(list(map(int, input().split())))
    
    # 문제: 주어진 좌표와 이동방향을 가지고 누구와 만나는지 어떻게 파악할까
    # grid를 쓸 필요가 없음
    # 원자들끼리 어느 방향으로 갔을때 누구와 만날 수 있는지 확인해야함
    # 우선순위가 있지
    # 어느 방향으로 간다는 정보가 있을때 그 방향으로 다른 원자들간 거리를 찾기, 누구와 만나는지 기록
    # 제일 짧은 거리의 원자 인덱스만 고려
    # 거리를 찾은 이후 거리값이 가장 짧은 순으로 원자를 없애면 됨
    #dfdfdf

    disappear_atoms = [False for _ in range(N)]
    distance_to_others = []
    for idx in range(N):
        distance, to_idx = find_min_distance(idx, atoms)


