T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    answer = 'No'

    for a in range(1, 10):
        for b in range(1, 10):
            if a * b == N:
                answer = 'Yes'
                break

        if answer == 'Yes':
            break

    print(f'#{tc} {answer}')