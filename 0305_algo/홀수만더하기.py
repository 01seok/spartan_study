T = int(input()) # 테스트 케이스 개수 입력 받기
for tc in range(1, T+1): # 각 테스트케이스 입력받기
    arr = list(map(int, input().split())) # 테스트 케이스 별 10개의 숫자 리스트로 받기
    result = 0 # 홀수만 더한 값을 담을 변수

    for num in arr: # 입력받은 10개 숫자 리스트를 num이 순회하며
        if num % 2 == 1: # 2로 나눈 나머지가 1이면 홀수니까
            result += num # 그 값들은 result에 더해주기
    
    print(f'#{tc} {result}')