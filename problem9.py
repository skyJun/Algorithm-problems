#스도쿠 검증

T = int(input())

for t in range(1, T+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    is_right = 1
    
    #행과 열 검증
    for i in range(9):
        if len(set(sudoku[i])) != 9 or len(set(row[i] for row in sudoku)) != 9:
            is_right = 0
            break
    
    if is_right:
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                grid_set = set()
                for i in range(3):
                    for j in range(3):
                        grid_set.add(sudoku[r + i][c + j])
                    
                if len(grid_set) != 9:
                    is_right = 0
                    break
            
            if is_right == 0:
                break
    
    print(f"#{t} {is_right}")