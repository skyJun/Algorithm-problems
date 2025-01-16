#쉬운 거스름돈
#각 종류의 돈이 몇 개씩 필요한지 출력
T = int(input())
money_units = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for t in range(1, T+1):
    N = int(input())
    money_cnt = []
    
    for unit in money_units:
        money_cnt.append(N // unit)
        N %= unit
    
    print(f"#{t}")
    print(" ".join(map(str, money_cnt)))