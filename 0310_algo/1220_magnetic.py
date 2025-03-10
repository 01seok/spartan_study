T = 10
for tc in range(1, T + 1):
    N = int(input()) # 100, 100 X 100 자석판
    board = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0 # 교착 상태 갯수
    
    # 세로 방향(열)로 교착을 봐야하므로
    for c in range(N):
        N_found = False
        # flag 변수, N극을 먼저 만나야 교착 가능하므로 N극 만난 상태인지 확인용 flag
        for r in range(N):  # 행 기준으로 아래로 내려가며 순회
            if board[r][c] == 1:    
                N_found = True  # N극 만나면 flag 변수 True 상태로 바꾸기
                
            if board[r][c] == 2:    # 그 후 2를 만난다면 교착
                if N_found:
                    cnt += 1    # 교착 + 1
                    N_found = False # 다음 교착 찾기 위해 다시 flag False로
                    
    print(f'{tc} {cnt}') 