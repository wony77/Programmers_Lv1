def solution(participant, completion):
    
    #선수 이름순으로 정렬
    participant.sort()
    completion.sort()
    
    # for문을 이용하여 순서가 같지 않은 친구를 찾아 출력 
    # 순서가 같지 않다는 것은 중간에 완주자에게는 없는 선수가 끼어있다는 차이를 이용함. 
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    
    #완주자 만큼 반복했는데 다 같았다면 참여자의 제일 마지막이 완주하지 못한 사람입니다.
    #리트스에서 -1은 제일 마지막을 의미한다. 
    return participant[-1]

#선수들을 받을 변수선언
participant_A = []
completion_A =[]

#선수 이름 받아서 participant_A의 리스트에 저장
while(True):
    B = input("선수 이름 입력: ")
    participant_A.append(B)
    
    if B == 'N':
        break

#완주 선수 이름 받아서 completion_A의 리스트에 저장
while(True):
    C = input("완주 선수 이름 입력: ")
    completion_A.append(C)
    
    if C == 'N':
        break

#완주하지 못한 선수 리턴받아 출력
print(solution(participant_A,completion_A))