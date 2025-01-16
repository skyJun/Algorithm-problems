#가위 1 바위 2 보 3
case = list(map(int,input().split()))

def decision(case):
    A_int = case[0]
    B_int = case[1]
    
    if A_int > B_int:
        if A_int == 3 and B_int == 1:
            return "B"
        return "A"
    else:
        if B_int == 3 and A_int == 1:
            return "A"
        return "B"

winner = decision(case)
print(winner)