T = int(input())  # 테스트 케이스 개수
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N 행 M 열
    arr = [list(map(int, input().split())) for _ in range(N)]  # 풍선 격자판 2차원 배열

    max_flower = 0  # 최대 풍선 터뜨린 값

    for r in range(N):
        for c in range(M):
            cnt = arr[r][c]  # 현재 위치의 풍선 값

            for d in range(4):  # 상하좌우 탐색
                nr = r + dr[d]
                nc = c + dc[d]
                if 0 <= nr < N and 0 <= nc < M:  # 배열 범위 내 확인
                    cnt += arr[nr][nc]

            max_flower = max(max_flower, cnt)  # 최대값 갱신

    print(f'#{tc} {max_flower}')  # 정답 출력
