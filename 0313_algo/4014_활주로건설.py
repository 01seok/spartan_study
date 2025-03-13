def build_runway(line, L):
    visited = [False] * N  # 경사로 설치 여부
    
    for i in range(1, N):
        if line[i] == line[i-1]:  # 높이 변화 없으면 다음 보러
            continue
        
        elif line[i] == line[i-1] + 1:  # 높이 1 증가 (뒤쪽 보기)
            for j in range(1, L+1):
                if i-j < 0 or line[i-1] != line[i-j] or visited[i-j]: 
                # 인덱스 범위 초과했거나 이전 숫자들이 다르거나 이미 경사로 설치했으면
                    return False  # 활주로 불가능
            for j in range(1, L+1):
                visited[i-j] = True  # 위에 조건문 뚫고 왔다면 경사로 설치

        elif line[i] == line[i-1] - 1:  # 높이 1 감소(앞쪽 보기)
            for j in range(L):
                if i+j >= N or line[i] != line[i+j] or visited[i+j]:  
                # 높이가 감소 했으니 인덱스 범위 초과 or 앞의 숫자들이 다르거나 경사로 설치한 적 있는지 검사
                    return False  # 활주로 불가능
            for j in range(L):
                visited[i+j] = True

        else:  # 높이 차이가 2 이상이면 경사로 의미 없으니 끝
            return False
    
    return True  # 활주로 설치

def count_runways(N, L, airport):
    cnt = 0
    
    # 행 기준 탐색
    for r in range(N):
        if build_runway(airport[r], L):
            cnt += 1

    # 열 기준 탐색
    for c in range(N):
        col = [airport[r][c] for r in range(N)]  # 각 열을 리스트로
        if build_runway(col, L):
            cnt += 1
    
    return cnt


T = int(input())
for tc in range(1, T + 1):
    N, L = map(int, input().split())
    airport = [list(map(int, input().split())) for _ in range(N)]

    print(f'#{tc} {count_runways(N, L, airport)}')