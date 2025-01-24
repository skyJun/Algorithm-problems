# 특이한 자석
# 4개의 자석, 각 자석 8개의 '날'
# 각 날 마다 N극 0, S극 1 자성
# 빨간색 화살표 index 0에 날 하나가 오도록 배치

# 신기한 규칙
# 임의의 자석 1칸 씩 K번 회전
# when 하나의 자석이 1칸 회전 if 붙어 있는 날의 자성과 다를 경우; 반대 방향 1칸 회전
# 붙어있다는 의미
# 2번 인덱스와 6번 인덱스 위치
# 예외 상황: 1번 자석과 4번 자석의 각각 6번 인덱스, 2번 인덱스는 고려 안함
# 2번 인덱스인 경우 +1 자석의 6번 인덱스
# 6번 인덱스인 경우 -1 자석의 2번 인덱스
# 회전 방향 시계방향 1, 반시계방향 -1

def rotate_magnet(magnets: list, magnet_index: int, 
                  rotate_direction: int, used_magnets: list) -> list:
    '''
    회전 방향 구현 함수

    return 값 바뀐 magents들의 배열 리스트
    '''
    start_magnets = magnets # 업데이트 하기 전 자석
    used_magnets[magnet_index] = True

    if magnet_index != 4 and not used_magnets[magnet_index + 1]:
        if start_magnets[magnet_index][2] != start_magnets[magnet_index + 1][6]:
            # 자성이 다르면 반대 회전
            magnets = rotate_magnet(start_magnets, magnet_index+1, -rotate_direction, used_magnets)

    if magnet_index != 1 and not used_magnets[magnet_index - 1]:
        if start_magnets[magnet_index][6] != start_magnets[magnet_index - 1][2]:
            # 자성이 다르면 반대 회전
            magnets = rotate_magnet(start_magnets, magnet_index-1, -rotate_direction, used_magnets)


    magnet = start_magnets[magnet_index]
    if rotate_direction > 0:
        # 시계방향 회전
        rotated_magnet = []
        for idx in range(8):
            if 0<= idx - rotate_direction:
                next_blade = magnet[idx - rotate_direction]
            else:
                next_blade = magnet[7]
            rotated_magnet.append(next_blade)
    else:
        # 시계 반대 방향 회전
        rotated_magnet = []
        for idx in range(8):
            if idx - rotate_direction < 8:
                next_blade = magnet[idx - rotate_direction]
            else:
                next_blade = magnet[0]
            rotated_magnet.append(next_blade)
    
    magnets[magnet_index] = rotated_magnet

    return magnets


# 점수 계산
# 1번 자석 빨간색 화살표 위치: N극 0 S극 1
# 2번 자석 빨간색 화살표 위치: N극 0 S극 2
# 3번 자석 빨간색 화살표 위치: N극 0 S극 4
# 4번 자석 빨간색 화살표 위치: N극 0 S극 8

T = int(input())
for t in range(1, T+1):
    K = int(input()) # 회전횟수

    # 자석 정보 입력
    magnets = [[-1 for _ in range(8)] for _ in range(5)]
    for magnet in range(1, 5):
        magnet_info = list(map(int, input().split()))
        magnets[magnet] = magnet_info
    
    # 회전
    for _ in range(K):
        used_magnets = [False for _ in range(5)]
        magnet_index, rotate_direction = input().split()
        magnets = rotate_magnet(magnets, int(magnet_index), int(rotate_direction), used_magnets)

    # 점수 계산
    result = 0
    for idx in range(1, 5):
        result += magnets[idx][0] * 2 ** (idx-1)

    
    print(f'#{t} {result}')

# 소요시간 2시간