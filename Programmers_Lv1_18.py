# Programmers_Lv1 실패율
# https://programmers.co.kr/learn/courses/30/lessons/42889

def solution(N,stages):
    fail ,fail1 , cnt  = [] , [] , 0 
    N_1 = len(stages)
    for i in range(1,N+1):
        cnt = stages.count(i)
        if cnt == 0:
            fail.append(0)
        else: 
            fail.append(cnt / N_1)
        N_1 -= cnt
        
    fail1 = sorted(fail,reverse=True)
    
    answer = []
    
    for i in range(len(fail)):
        answer.append(fail.index(fail1[i])+1)
        fail[fail.index(fail1[i])] = -1
        
    return answer

N = int(input('모든 스테이지 수: '))
stage = list(map(int,input('도전자들의 스테이지: ').split()))

print(solution(N,stage))