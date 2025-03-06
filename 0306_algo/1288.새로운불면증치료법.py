T = int(input())
for tc in range(1, T+1):
    N = int(input())
    zero_to_nine = set()    # 0~9까지 담을 세트, 중복 방지, 얘네가 0 ~ 9 까지 차면 종료

    k = 0   # N에 곱해줄 k 값 초기화 세팅
    while len(zero_to_nine) < 10:   # 종료조건은 0~9까지 차면 종료
        k += 1  # while문  한바퀴 돌 때마다 k값 1증가, 종료조건 만족할 때 까지 계속 진행
        result = str(N * k) # 숫자를 중복 없이 담기위해 문자열로 변환
        zero_to_nine.update(result) # 0~9까지 담을 set에 곱해져나온 값 문자열로 update ( 중복 없음 )

    print(f'#{tc} {N*k}')