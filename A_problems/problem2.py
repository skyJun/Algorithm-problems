# 보물상자 비밀번호

# 16진수 숫자가 적혀있는 보물 상자
# 각 변에는 동일한 개수의 숫자가 있고 시계방향 순으로 높은 자리 숫자에 해당
# 보물상자에는 자물쇠가 걸려 있는데. 이 자물쇠의 비밀번호는
# 보물 상자에 적힌 숫자로 만들 수 있는 모든 수 중, K번째로 큰 수를 10진수로 만든수

T = int(input())

for t in range(1, T+1):
    numbers = input()
    numbers_length = len(numbers)

    numbers_list = [char for char in numbers]
    number_16_set = set()
    while True:
        numbers_list[]
