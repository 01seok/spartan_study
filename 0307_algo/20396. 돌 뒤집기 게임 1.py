T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # N: 돌의 개수, M: 뒤집기 반복 횟수
    arr = list(map(int, input().split()))   # 초기 돌 상태 리스트 입력 받기
    
    for _ in range(M):  # M번 뒤집기 때문에 M번 만큼 반복
        i, j = map(int, input().split())    # i번째부터 j개의 돌을 i번째 돌 색 깔로 바꿔야함
        
        i = i - 1   # i번째를 인덱스로 써야하니 - 1
        for s in range(i, i+j): # s가 i번째 돌에서부터 j번째 돌까지만 돌면서
            if s < N:   # s가 리스트 범위 벗어나지 않게 범위 설정
                arr[s] = arr[i] # s번째 돌이 출발 돌 i랑 같아짐
    
    print(f'{tc}', * arr)   # 빈칸 구분 출력