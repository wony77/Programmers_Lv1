# Programmers Lv1 탐욕법 > 체육복

def solution(n, lost, reserve):
    # 원소에서 중복된 친구를 제거하기 위한 set함수 활용
    set_reserve = set(reserve) - set(lost)
    set_lost = set(lost) - set(reserve)

    # 여벌을 가지고 있는 친구를 한명씩 i에 할당
    for i in set_reserve:
        # 여벌 옷을 가지고 있는 i를 기준으로 
        # i-1 번째 친구가 옷이 없을 경우 
        # lost_set 의 원소를 지워주므로써 빌려주는것을 표시
        if i-1 in set_lost:
            set_lost.remove(i-1)
        # 여벌 옷을 가지고 있는 i를 기준으로 
        # i+1 번째 친구가 옷이 없을 경우 
        # lost_set 의 원소를 지워주므로써 빌려주는것을 표시    
        elif i+1 in set_lost:
            set_lost.remove(i+1)
    
    # set_lost에 남은 학생은 옷을 빌리지 못한 학생으로 
    # 전체 학생에서 set_lost의 길이를 빼주면 옷을 가지고 있는 친구만 남게 된다.
    answer = n - len(set_lost)

    return answer

student = int(input('전체 학생 수: '))
lost_student = list(map(int,input('도난 당한 학생 번호: ').split()))
reserve_student = list(map(int,input('여벌의 체육복을 가진 학생: ').split()))

print(solution(student,lost_student,reserve_student))