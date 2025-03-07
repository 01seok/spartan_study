T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # 돌 갯수 N, 뒤집기 횟수 M 입력받기
    arr = list(map(int, input().split()))   # 초기 돌 리스트 입력받기
    
    for _ in range(M):  # M번 뒤집을거니까 M번 반복
        i, j = map(int, input().split())    # i번째 돌을 기준으로 j번째 돌까지 확인 후 뒤집기
        i -= 1  # 인덱스로 사용해야하니 -1
        for r in range(1, j+1):    # r이 i를 기준으로 j번째 돌까지 확인해야하니 +1, 중심 돌 들어가면 안됨
            left = i - r    # i번째 돌 기준 왼쪽
            right = i + r   # i번째 돌 기준 오른쪽

            if left < 0 or right >= N:  # 리스트 벗어나지 않게 범위 설정
                break

            if arr[left] != arr[right]: # 좌우 다르다면 다음 r 보러가기
                continue
            
            if arr[left] == arr[right]: # 좌우 같으면 반전 시켜주기
                arr[left], arr[right] = 1 - arr[left], 1 - arr[right]
    
    print(f"#{tc}", *arr)