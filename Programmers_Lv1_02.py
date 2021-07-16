# 카카오 인턴 코딩테스트 ' 키패드 누르기 '

# 키패드 왼손으로 누를 지 오른손으로 누를지 판별 함수
def solution (Phone_number,hand_RL):
    # 변수 선인 및 초기화
    # 전화 키패드 (딕셔너리)
    KeyPad = { 1 : [0,0], 2 : [0,1], 3 : [0,2],
               4 : [1,0], 5 : [1,1], 6 : [1,2],
               7 : [2,0], 8 : [2,1], 9 : [2,2],
               '*' : [3,0], 0 : [3,1], '#' : [3,2]}
    # 왼손 오른손 시작 좌표 저장
    L = [3,0]
    R = [3,2]
    M = []
    # 왼손 오른손 확정으로 누르는 번호 저장
    L1 = [1,4,7]
    R1 = [3,6,9]
    # 눌른것이 오른손인지 왼손인이 저장하기위한 변수
    KeyPush = []
    # Hand_RL << 거리가 같을 때 자주 쓰는 손을 우선하기 위한 변수
    L_Distance = 0
    R_Distance = 0
    cnt = -1

    # L R누르는 판별문
    for i in Phone_number:
        #왼손과 오른속 확정으로 누를 수 있는것들 먼저 처리
        if i in L1:
            KeyPush.append('L')
            L = KeyPad[i]
        elif i in R1:
            KeyPush.append('R')
            R = KeyPad[i]
        else:
            M = KeyPad[i]
            # 오른손과 왼손이 중앙 키패드 까지의 거리를 구합니다.
            L_Distance = abs(L[0]-M[0])+abs(L[1]-M[1])
            R_Distance = abs(R[0]-M[0])+abs(R[1]-M[1])

            # 거리 판별해서 Key Push에 추가합니다.
            if L_Distance < R_Distance:
                KeyPush.append('L')
                L = KeyPad[i]
            elif R_Distance < L_Distance:
                KeyPush.append('R')
                R = KeyPad[i]
            else:
                if hand_RL == 'L':
                    KeyPush.append('L')
                    L = KeyPad[i]
                else:
                    KeyPush.append('R')
                    R = KeyPad[i]
        # 거리는 계속 사용해야 하므로 초기화 시켜줍니다.            
        L_Distance = 0
        R_Distance = 0
    answer = "".join(KeyPush)
    return answer

# 전화 번호 입력 받는 곳
P_number= list(map(int,input("전화번호 입력해주세요: ")))

# 오른손 잡이 왼손 잡이 받는 곳
while(True):
    hand = input("왼손잡이(L)/오른손잡이(R): ")
    if hand == 'L' or hand == 'R':
        break
    else:
        print("다시 입력 부탁드립니다. ")

print(solution(P_number,hand))

