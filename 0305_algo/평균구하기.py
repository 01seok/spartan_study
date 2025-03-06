T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))

    nums = sum(arr) / len(arr) # 리스트의 값들을 더한 값에서 리스트의 길이를 나눠서 평균을 구함
    result = int(round(nums)) # 정답으로 출력할 result에 round 함수를 사용해서 소수점 첫째 자리에서 반올림, 실수에서 정수로 변환
    print(f'#{tc} {result}')