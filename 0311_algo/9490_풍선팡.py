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
            power = arr[r][c]   # 처음 터진 풍선에 들어있는 꽃가루 만큼 퍼져나가며 터질거임
            for d in range(4):  # 상하좌우 탐색
                for k in range(1, power+1): # 0은 이미 터진자리니까 1부터 출발
                    nr = r + dr[d] * k  # k 만큼 나아가며 터트리기
                    nc = c + dc[d] * k
                    if 0 <= nr < N and 0 <= nc < M:  # 배열 범위 내 확인
                        cnt += arr[nr][nc]

            max_flower = max(max_flower, cnt)  # 최대값 갱신

    print(f'#{tc} {max_flower}')
