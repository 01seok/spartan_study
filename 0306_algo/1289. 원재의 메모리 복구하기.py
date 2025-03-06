T = int(input())
for tc in range(1, T+1):
    target = list(map(int, list(input())))  # 목표 상태 리스트로 입력 받기
    n = len(target) # 처음에 0만 가득한 메모리 만들어야하니 길이 구하기
    
    memory = [0] * n  # 처음 시작할 메모리 리스트
    cnt = 0  # 뒤집은 횟수 저장할 변수
    
    while memory != target: # 같아지면 while문 탈출
        for i in range(n):  # i가 타겟 길이 만큼 순회하며 다른 값 찾기 (뒤집기 시작할 값)
            if memory[i] != target[i]:
                break   # 다른거 찾았으니 뒤집을 반복문으로 이동

        for j in range(i, n):   # 다른 값 i부터 끝까지 뒤집어주기
            memory[j] = 1 - memory[j]   # 뒤집기

        cnt += 1

    print(f"#{tc} {cnt}")