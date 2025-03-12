T = int(input())
for tc in range(1, T + 1):
    arr = input().split()
    N = int(arr[0]) # 버튼 개수
    order = arr[1:] # 버튼 누르는 명령 리스트
    
    O_position, B_position = 1, 1    # O, B의 출발점
    O_time, B_time = 0, 0   # O, B가 버튼 누르기 전의 시간 
    # 이전 작업에서 썼던 시간이니 연속 작업을 하면 이 숫자를 기준으로 할거고 다른 로봇이 작업했다면
    # 이 시간은 아래의 max를 이용해서 갱신 될 것
    time = 0    # 총 소요된 시간
    
    for i in range(N):
        robot, target = order[2 * i], int(order[2 * i + 1])

        if robot == 'O':
            move_time = abs(target - O_position)
            
            # 이 로봇이 이전에 있던 위치에서 타겟의 위치를 뺀 값과 이동 시간을 더해도 
            # 다른 로봇이 움직이며 소요한 시간이 더 크다면 시간은 그 시간에 맞춰지니 소요 시간은 맞게 떨어짐
            # 즉, 실제로 로봇이 이동하지 않았더라도 다른 로봇이 소요한 시간이 반영 되어서 전체 시간 흐름 맞음
            O_time = max(O_time + move_time, time) + 1    # 버튼 누르는데 1초 걸리니 1 더해주기
            O_position = target
            time = O_time
            
        else:   # 블루가 움직일 순서라면
            move_time = abs(target - B_position)
            B_time = max(B_time + move_time, time) + 1
            B_position = target
            time = B_time
            
    print(f'#{tc} {time}')