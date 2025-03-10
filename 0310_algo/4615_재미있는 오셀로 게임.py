T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())    # 보드 길이 N X N, 플레이어 돌 놓는 횟수 M ( 한 보드 판에서 반복할 횟수 M )
    board = [[0] * N for _ in range(N)] # 보드 판 2차원 배열로 입력 받기
    mid = N // 2    # 보드 판의 중간
    board[mid - 1][mid - 1], board[mid][mid] = 2, 2 # 백돌 초기 위치
    board[mid][mid - 1], board[mid - 1][mid] = 1, 1 # 흑돌 초기 위치

    # 델타 배열, 상하좌우 좌상 우상 좌하 우하 (대각선)
    dr = [-1, 1, 0, 0, -1, -1, 1, 1]
    dc = [0, 0, -1, 1, -1, 1, -1, 1]

    for _ in range(M):
        r, c, color = map(int, input().split()) # (r,c), color type 1 or 2
        r -= 1
        c -= 1

        board[r][c] = color # 좌표에 돌 놓기

        for d in range(8): # 8방향 델타 탐색
            nr, nc = r + dr[d], c + dc[d]
            flip_lst = []   # 뒤집을 좌표 저장할 리스트, 같은 color 있어야 뒤집기 때문에 일단 리스트에 담아두자

            while 0 <= nr < N and 0 <= nc < N and board[nr][nc] != 0:   # 범위 설정
                if board[nr][nc] == color:  # 계속 가다가 같은 color가 있다면?
                    for fr, fc in flip_lst: # fr, fc가 후보 리스트를 반복하며
                        board[fr][fc] = color   # 같은 색으로 바꿔주기
                    break

                else:
                    flip_lst.append((nr, nc))  # 다른 색이면 리스트에 담아두고
                # 계속 탐색하러가자
                nr += dr[d]
                nc += dc[d]

    a = sum(row.count(1) for row in board)  # 행 별로 돌면서 1이 몇갠지 세어보기
    b = sum(row.count(2) for row in board)  # 행 별로 돌면서 2가 몇갠지 세어보기

    print(f'#{tc} {a} {b}')