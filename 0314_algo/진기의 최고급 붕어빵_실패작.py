T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    guest_time = list(map(int, input().split()))
    
    guest_time.sort()
    guest_num = 0
    
    fish_persec = K // M
    total_fish = 0
    
    flag = True
    for time in range(guest_time[-1] + 1):
        total_fish += fish_persec
        
        while guest_num < N and guest_time[guest_num] == time:
            if total_fish > 0:
                total_fish -= 1
                guest_num += 1
                
            else:
                print(f'#{tc} Impossible')
                flag = False
                break
        if not flag:
            break
    if flag:
        print(f'#{tc} Possible')