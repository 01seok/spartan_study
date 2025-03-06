'''
1. 마름모를 삼각형 두개로 나눠서 처리
- 위쪽 삼각형 : 높이는 N // 2에서 시작해서 0까지 줄어듬
- 아래쪽 삼각형 : N // 2에서 시작해서 N-1까지 증가
시작점 같으므로 끝날 때 N // 2줄에 있는 sum 빼주기

2. 슬라이싱을 이용해서 풀기위해 s, e 범위 설정
위쪽 삼각형 s는 감소 e는 증가
아래 삼각형 s 증가 e는 감소
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

마지막 total -= sum(arr[N//2][s:e+1])
total 출력
'''
T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 농장 크기: N
    arr = [list(map(int, input())) for _ in range(N)] # 농장 2차원 배열

    total = 0
    s, e = N // 2, N // 2   # start, end는 배열 크기의 중간에서 시작
    r = N // 2 # 중간 행부터 시작

    # 위쪽 삼각형
    while r >= 0:
        total += sum(arr[r][s:e+1])
        s -= 1
        e += 1
        r -= 1

    s, e = N // 2, N // 2
    r = N // 2

    # 아래쪽 삼각형
    while r < N:
        total += sum(arr[r][s:e+1])
        s += 1
        e -= 1
        r += 1

    s, e = N // 2, N // 2
    r = N // 2

    total -= sum(arr[r][s:e+1])

    print(f'#{tc} {total}')