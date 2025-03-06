T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 숫자 N
    nums = [2, 3, 5, 7, 11] # N을 구성하고 있는 소인수들 ( 얘네 곱하면 N 나옴 )
    result = [] # 지수 담을 리스트

    for i in nums:  # i가 소인수들 순회하면서 하나씩 나눠볼거
        pow = 0 # 지수 초기 값 0, while문 한번 돌았다 = 한번 나눠진다 = 지수 + 1
        while N % i == 0:   # 나눴을 때 나머지 없이 깔끔하게 나온다면, 나머지 나오면 다음 소인수로 넘어가기
            N //= i         # N을 소인수 i로 나누고
            pow += 1        # 지수 1 추가
        result.append(pow)  # while문 끝나고 해당 소인수 몇번 나눴는지 카운트 한 값 = 해당 소인수의 지수

    print(f'#{tc}', *result)    # 공백 구분 출력