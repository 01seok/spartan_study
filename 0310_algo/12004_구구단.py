T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    answer = 'No'   # 찾았는지에 대한 기본 값(정답) No로 설정

    for a in range(1, 10):  # 1 ~ 9 까지 숫자를 순회하며
        for b in range(1, 10):  # 1 ~ 9 숫자 1 x 1, 1 x 2, 1 x 3 ... 9 x 9까지 순회하게 이중 반복문
            if a * b == N:  # 둘이 곱해서 찾는 숫자 N이 나온다면
                answer = 'Yes'  # 찾았으니 Yes로 변경
                break   # 찾았으니 내부 반복문 break

        if answer == 'Yes': # answer가 Yes 라면
            break   # 외부 반복문도 break

    print(f'#{tc} {answer}')