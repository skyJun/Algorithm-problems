# 벽돌깨기
# 구슬 N번만 쏠 수 있음
# 벽돌의 정보는 W H 배열로 주어짐
# 0은 빈 공간, 그 외의 숫자는 벽돌을 의미

# 구슬은 좌, 우로만 움직일 수 있고 항상 맨 위에 있는 벽돌만 깨트릴 수 있음
# 벽돌은 1 ~ 9로 표현
# 구슬이 명중한 벽돌은 상하좌우로 벽돌에 적힌 숫자 -1 칸만큼 같이 제거 됨
# 연쇄 작용도 발생
# 벽돌이 없어지면 남은 벽돌은 아래로 하강
# 최대한 많은 벽돌을 제거하려고 함
# 남은 벽돌의 개수를 구하라 -> 남은 벽돌의 수가 최소인 것을 찾는게 목표
import sys 
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for t in range(1, T+1):
    N, W, H = tuple(map(int, input().split()))

    grid = [list(map(int, input().split())) for _ in range(H)]
    print(N, W, H)
    print(grid)