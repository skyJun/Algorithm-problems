N = int(input())
scores = sorted(list(map(int, input().split())))

print(scores[N//2])