T = int(input())
for tc in range(1, T + 1):
    N, Q = map(int, input().split())    # 상자 개수 N개, 반복 횟수 Q번
    boxes = [0] * N

    for i in range(1, Q+1): # 1부터 시작해야 Q번 반복하는 동안 숫자가 올바르게 변경 됨
        L, R = map(int, input().split())    # L번부터  R번까지 Q의 반복 횟수 숫자로 변경

        for j in range(L-1, R): # 다시 인덱스로 접근해야하므로 L번째 = L - 1
            boxes[j] = i    # Q만큼 돌고있는 외부 반복문의 숫자로 변경!

    print(f'#{tc}', * boxes)    # 출력형식 고려