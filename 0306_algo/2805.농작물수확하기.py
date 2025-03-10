'''
1. 마름모를 삼각형 두개로 나눠서 처리
- 위쪽 삼각형 : 높이는 N // 2에서 시작해서 0까지 줄어듬
- 아래쪽 삼각형 : N // 2에서 시작해서 N-1까지 증가
시작점(중앙)같으므로 끝날 때 N // 2줄에 있는 sum 빼주기

2. 슬라이싱을 이용해서 풀기위해 행의 start, end 범위 설정
삼각형 s는 증가 e는 감소
각 행 유효범위 arr[r][s:e+1]로 슬라이싱

3. total = 0
- 위 삼각형 while r >= 0:
total += sum(arr[r][s:e+1])

s -= 1, e+= 1
r -= 1

- 아래 삼각형
while r < N:
total += sum(arr[r][s:e+1])
s += 1, e -= 1
r += 1

마지막 total 중복 값 빼주기
total 출력
'''
T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 농장 크기: N
    arr = [list(map(int, input().strip())) for _ in range(N)]  # 농장 2차원 배열 N x N 사이즈 리스트로 입력받기

    total = 0   # 정사각형 마름모 안의 값들 더할 변수
    
    # 위쪽 삼각형 (중앙행부터 위쪽으로 더해나감)
    s, e = 0, N - 1     # 시작점 0, 끝지점 N-1 (인덱스이기 때문에 -1)
    r = N // 2          # 행의 위치는 전체 크기의 절반 지점
    while r >= 0:       # 최상단 행까지 가면 while문 종료
        total += sum(arr[r][s:e+1])    # 슬라이싱을 이용해서 r행의 시작부터 끝지점까지, 리스트 슬라이싱할 땐 뒤에 값 앞까지 가니 + 1
        s += 1      # 다 더했으니 다음 행에선 한칸씩 좁혀야하니 s, e 값 변경해두고
        e -= 1
        r -= 1      # 다음 행으로 올라가기

    # 아래쪽 삼각형 (중앙행부터 아래쪽)
    s, e = 0, N - 1 
    r = N // 2
    while r < N:
        total += sum(arr[r][s:e+1])
        s += 1
        e -= 1
        r += 1      # 여기선 밑으로 내려가는 구조이니 행 + 1씩 내려가기

    # 중앙행 중복 됐으니 한번 빼주기
    total -= sum(arr[N//2][0:N])

    print(f'#{tc} {total}')