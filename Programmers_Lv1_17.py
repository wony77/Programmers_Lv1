# Programmers_Lv1 로또의 최고 순위와 최저 순위
# https://programmers.co.kr/learn/courses/30/lessons/77484

# 문제 이해를 잘못하면 이렇게 푸는 풀이입니다...
# 귀엽게 봐주세요...
import random
def solution(lottos, win_nums):
    answer, answer1 = [], []
    cnt, k = 0 , 0
    max1 = list(lottos)
    min1 = list(lottos)

    # 딕셔너리에 로또 등수를 저장합니다.
    winner = {0 : 6,
              1 : 6,
              2 : 5,
              3 : 4,
              4 : 3,
              5 : 2,
              6 : 1}

    # 최대 등수 만들기
    # lotto 번호수 만큼 반복합니다.
    for i in range(len(max1)):
        # 만약 max1 리스트에 있는 원소가 0이면
        if max1[i] == 0:
            # 무한반복문을 시작해줍니다.
            while (True):
                # 당첨 번호에서 랜덤으로 숫자를 하나 가져와 k에 할당합니다.
                k = random.choice(win_nums)
                # 만약 max1리스트에 존재하지 않은 숫자이면 0 을 k로 바꿔줍니다.
                # 아래와 같은 조건을 사용한 이유는 로또에는 중복 번호가 없기 때문입니다.
                if k not in max1:
                    max1[i] = k
                    break
    # 당첨 번호와 같은 번호가 몇개인지 새어주는 반복문 입니다.
    for i in max1:
        if i in win_nums:
            cnt += 1 
    # answer라는 친구에 카운트를 추가해 줍니다.
    answer.append(cnt)
    # min1을 만들때 사용하기위해 초기화 해줍니다.
    cnt = 0

    # 최소 등수 만들기
    # 내용은 위와 같습니다.
    for i in range(len(min1)):
        if min1[i] == 0:
            while (True):
                # 1~45 사이의 수 중 랜덤으로 하나 가지고 옵니다.
                k = random.randrange(1,46)
                # 이 수는 min1에도 당점번호에도 없어야 하는 수여야 합니다.
                if k not in min1 and k not in win_nums:
                    min1[i] = k
                    break        
    # min과 당첨 번호를 비교해줍니다.
    for i in min1:
        if i in win_nums:
            cnt += 1 
    answer.append(cnt)

    # 등수를 판별할 차례입니다.
    # 몇개의 번호가 같은지 저장되어있는 리스트를 가져옵니다.
    for i in answer:
        # 등수가 저장된 딕셔너리에서 key값과 value값을 가져옵니다.
        for key, value in winner.items():
            # 만약 i 가 key값과 같으면 value값을 저장해줍니다.
            if i == key:
                answer1.append(value)
    return answer1

lotto = list(map(int,input('로또 번호: ').split()))
win_num = list(map(int,input('당첨 번호: ').split()))

print(solution(lotto,win_num))