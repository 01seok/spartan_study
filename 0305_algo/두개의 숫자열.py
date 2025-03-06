T = int(input())

# 테스트 케이스 수만큼 반복
for tc in range(1, T+1):
    N, M = map(int, input().split())    # N: 숫자열 A의 길이, M: 숫자열 B의 길이
    # 숫자열 A
    A = list(map(int, input().split()))
    # 숫자열 B
    B = list(map(int, input().split()))

    # 최대 곱의 합을 저장할 변수, 음수도 고려해야 하므로 가장 작은 값으로 세팅
    max_v = float('-inf')

    if N < M:   # 만약 A가 B보다 짧다면, 두 숫자열을 바꿔서 A가 항상 긴 숫자열이 되도록 조정
        N, M = M, N  # 두 숫자열의 길이 교환
        A, B = B, A  # 두 숫자열 자체를 교환하여 항상 A가 긴 배열이 되게 함

    # A에서 B를 이동시키면서 최대 곱의 합 찾기
    for i in range(N-M+1):  # 긴 배열 A에서 비교 할 위치 0 ~ N-M
        s = 0  # (갱신 시켜줄) 곱셈 값 담을 변수

        for j in range(M):  # 짧은 배열 B의 모든 원소를 하나씩 곱함
            s += A[i+j] * B[j]  # A의 부분구간과 B의 원소를 곱해서 s에 더해주기

        if max_v < s:   # 현재까지 찾은 최대 곱의 합과 비교하여 더 크다면 갱신
            max_v = s
    print(f'#{tc} {max_v}')