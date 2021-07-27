# Programmers_Lv1 예산 < 그리디 알고리즘
# https://programmers.co.kr/learn/courses/30/lessons/12982

def solution(d1, budget1):
    # 한정된 자원으로 최대한을 뽑아야 하기 때문에 오름차순으로 정렬
    d1.sort()
    answer = 0
    # 정해진 예산에서 하나씩 빼주기 위해서 for 문을 돌림
    for d2 in d1:
        # 예산이 0원 보다 크거나 같을때 까지만 진행하는 반복문
        # +@ 몇개의 부서가 지원되는지 확인해줄 answer 카운트
        if budget1 - d2 >= 0:
            budget1 -= d2
            answer+=1
        else:
            break
    return answer

d = list(map(int,input('각 부서가 원하는 금액: ').split()))
budget = int(input('지원하는 예산: '))

print(solution(d,budget))