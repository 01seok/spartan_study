T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    guest_time = sorted(list(map(int, input().split())))
    
    current_fish = 0    # 현재 보유 중인 붕어빵 수
    guest_num = 0       # 손님 번호(인덱스로 쓸)
    flag = True         # flag변수 impossible 나오면 탈출용
    
    # 0초부터 마지막 손님 오는 시간까지 반복문
    for time in range(guest_time[-1] + 1):
        # 0초에는 붕어빵 없음, M초마다 K개의 붕어빵 생산
        if time > 0 and time % M == 0:  # 나눴을 때 나머지 없다 => 입력으로 주어진 붕어빵 생성 시간이다
            current_fish += K   # k개 보유 중인 붕어빵에 추가
        
        # 손님 숫자가 오기로 한 N명 일 때 까지 while문, 손님 오기로 한 시간과 지금 시간이 일치할 때 실행
        while guest_num < N and guest_time[guest_num] == time:
            if current_fish <= 0:   # 붕어빵 만들어둔거 없으면 불가능
                print(f'#{tc} Impossible')
                flag = False
                break
            if current_fish >= 0:   # 붕어빵 남아있다면
                current_fish -= 1   # 붕어빵 한 마리 빼고
                guest_num += 1  # 다음 손님 받으러 가기
            
        if not flag:    # while문도 종료
            break
        
    if flag:
        print(f'#{tc} Possible')