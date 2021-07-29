def solution(answers):
    # 1번 2번 3번의 찍는 번호 규칙 저장한 2차원 배열
    aa = [[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]

    # 변수 선언 및 초기화
    aa1, answer1, answer2, answer = [], [], [], []
    cnt = 0

    # 찍는 번호의 수를 정답 수 만큼 만들어 주는 과정
    # [0] 행부터 ~ [2]행 까지 한 행씩 불러와 동작 
    for i in aa:
        # avg에 졍답의 길이를 i로 나눈 값에 +1을 해줍니다. 
        # +1을 해주지 않으면 찍는 번호의 수는 정답 만큼 늘어나지 않습니다.
        avg = len(answers)//len(i) + 1
        # i * avg 를 하여 찍는 번호를 늘려줍니다.
        aa1.append(i*avg)

    # 정답과 비교하여 몇개가 맞는지 확인하는 for문
    # [0] 행부터 ~ [2]행 까지 한 행씩 불러와 동작 
    for i in aa1 :
        # 정답의 길이만큼 반복합니다.
        for j in range(len(answers)):
            # 만약 정답의 j인덱스와 찍은 번호의 j인덱스가 같으면
            if i[j] == answers[j]:
                # cnt를 1씩 증가시켜줍니다.
                cnt+=1
        #그리고 cnt만 저장해줄 변수에 추가해주고 cnt를 초기화 해줍니다.
        answer1.append(cnt)
        cnt = 0
    
    # answer2 라는 변수에 카운트가 가장 큰 수를 저장해줍니다.
    answer2.append(max(answer1))

    # 가장 많이 맞춘 사람 찾기
    # 카운트가 든 변수 만큼 반복할 것이고
    for i in range(len(answer1)):
        # 카운트 최대값과 같으면 answer에 가장 큰 값이 어디 있는지 판별해주는 조건문입니다. 
        # +1을 해주는 이유는 i는 0부터 시작이기 때문입니다.
        if answer1[i] == answer2[0]:
            answer.append(i+1)
    return answer

answer =list(map(int,input('정답을 입력해주세요: ').split()))
print(solution(answer))