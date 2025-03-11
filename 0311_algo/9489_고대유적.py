T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())    # N행, M열
    field = [list(map(int, input().split())) for _ in range(N)]
    
    max_len = 0 # 고대 유적 최대 길이(정답)
    
    # 행 우선 탐색
    for r in range(N):
        length = 0  # 현재 행에 있는 고대 유적의 길이(만약 0이 나와도 뒤에 더 있을 수도 있음)
        for c in range(M):
            if field[r][c] == 1:    # 1이 있다면 고대 유적 길이 1 추가하고 계속 탐색
                length += 1
            else:   # 0이 나온다면 지금까지의 길이와 최대 길이 비교 후 갱신 된다면 갱신
                max_len = max(max_len, length)
                length = 0  # 다음을 위해 초기화
                
        # 1로 끝났다면 갱신 안됐으니 행 다 돌고 나서 최대 길이 갱신
        max_len = max(max_len, length)
    
    # 열 방향 탐색
    for c in range(M):
        length = 0
        for r in range(N):
            if field[r][c] == 1:
                length += 1
            else:
                max_len = max(max_len, length)
                length = 0
        # 마찬가지로 1로 끝났으면 열을 다 돌고 나서도 최대 길이 갱신
        max_len = max(max_len, length)
    
    print(f"#{tc} {max_len}")