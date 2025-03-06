T = int(input())
score = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

for tc in range(1, T+1):
    N, K = map(int,input().split())
    students = []


    for i in range(N):
        mid, fin, hw = map(int, input().split())
        scores = 0.35 * mid + 0.45 * fin + 0.2 * hw
        students.append([scores, i+1])  # 성적 비율 반영된 총점, 학생번호
    
    for i in range(N-1):    # 성적을 비교하기 위한 반복문
        for j in range(i+1, N): # i 다음 번호부터 비교해야하므로 범위 설정 i+1
            if students[i][0] < students[j][0]:
                students[i],students[j] = students[j],students[i]   # 더 큰 점수가 앞으로 오도록 자리 바꾸기

    per_group = N // 10     # 등급 당 인원 N // 10
    idx = 0

    for i in range(10):     # 등급 부여를 위해 10개의 등급 i가 순회하며
        for j in range(per_group):  # 등급 당 인원만큼 j가 돌면서 등급 정해줌
            students[idx].append(score[i])  # 큰 점수가 앞에 나와 있으니 같이 성적 부여
            idx += 1    # 성적 부여가 끝나면 다음 학생 성적 부여하기 위해 idx += 1

    
    for i in range(N-1):    # 등급 부여가 끝났으니 성적순으로 배열 해놨던 students를 학생 번호 순으로 다시 돌려주기
        for j in range(i+1, N): 
            if students[i][1] > students[j][1]: # 학생 번호 순으로 재정렬해주기
                students[i], students[j] = students[j], students[i]

    
    print(f'#{tc} {students[K-1][2]}')  # K번째 학생의 번호는 인덱스상으로 K-1, 2번 인덱스 등급 출력