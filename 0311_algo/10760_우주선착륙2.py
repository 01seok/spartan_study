T = int(input())

# 상 하 좌 우 좌상 우상 우하 좌하
dr = [-1, 1, 0, 0, -1, -1, 1, 1]
dc = [0, 0, -1, 1, -1, 1, 1, -1]

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    mars = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0 # 최종 후보지 (정답)
    for r in range(N):
        for c in range(M):
            start = mars[r][c]  # 출발지 정해두고 델타 탐색 시작
            land_area = 0   # 예비 후보지 4개 넘으면 cnt + 1 시킬 변수
            for d in range(8):  # 8방향 탐색
                nr, nc = r + dr[d], c + dc[d]
                if 0 <= nr < N and 0 <= nc < M: # 범위 체크
                    if start > mars[nr][nc]:    # 착륙지보다 낮은 곳이라면
                        land_area += 1  # 예비 후보지 1곳 추가
            if land_area >= 4:  # 예비 후보지 4곳 이상이라면
                cnt += 1    # 최종 후보지 1곳 추가
    print(f'#{tc} {cnt}')