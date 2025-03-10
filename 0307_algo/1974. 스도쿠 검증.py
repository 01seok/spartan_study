def sdoku(puzzle):  # 스도쿠 검증하는 함수
    for r in range(9):  # 행 순회해서 가로부터 중복있는지 체크
        nums = set()    # 한번 나온 숫자들 체크 할 set, 이 위치에서 초기화 되어야 행이 바뀔 때 마다 제대로 검사 가능함
        for c in range(9):  
            num = puzzle[r][c]
            if num in nums:
                return 0
            nums.add(num)   # 중복 되지 않았다면 set에 넣어주기
    
    for c in range(9):  # 열 순회해서 세로도 중복 있는지 체크해주기
        nums = set()    # 마찬가지로 이 위치에서 초기화 되어야 한개 열 도는 동안만 체크하는 set로 동작
        for r in range(9):
            num = puzzle[r][c]
            if num in nums:
                return 0
            nums.add(num)
    
    # 9칸 검사 끝났으니 각 3 x 3 박스도 검사
    for row in range(0, 9, 3):  # 0부터 8까지 9칸을 3칸 단위로 돌기
        for col in range(0, 9, 3):
            small_nums = set()
            for r in range(row, row + 3):   # 그 반복문 안에서 0 ~ 3, 3 ~ 6, 6 ~ 9 진짜 3x3검사 시작
                for c in range(col, col + 3):
                    small_num = puzzle[r][c]
                    if small_num in small_nums:
                        return 0
                    small_nums.add(small_num)
    
    # 3개 다 통과하면 1 return
    return 1

T = int(input())
for tc in range(1, T+1):
    puzzle = [list(map(int, input().split())) for _ in range(9)]
    result = sdoku(puzzle)
    print(f'#{tc} {result}')