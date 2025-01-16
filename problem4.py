T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    if N < M:
        short_arr, long_arr = A, B
    else:
        short_arr, long_arr = B, A
    
    len_s = len(short_arr)
    len_l = len(long_arr)
    
    max_sum = float('-inf')
    for start in range(len_l - len_s + 1):
        cur_sum = 0
        for k in range(len_s):
            cur_sum += short_arr[k] * long_arr[start + k]
        
        if cur_sum > max_sum:
            max_sum = cur_sum
    
    print(f"#{t+1} {max_sum}")