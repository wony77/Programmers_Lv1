# Programmers_lv1 나누어 떨어지는 숫자 배열
# https://programmers.co.kr/learn/courses/30/lessons/12910

def solution(arr, divisor):
    # 변수 선언 및 초기화
    answer = []
    cnt = 0

    # 받은 배열을 하나씩 불러와 반복
    for i in arr:
        # 만약 divisor로 나눈 나머지가 0일경우
        if i % divisor==0:
            # answer에 i를 추가해줍니다.
            answer.append(i)
            cnt += 1
    # 카운트가 0인경우는 나누어 떯어지는 수가 없다는 뜻이므로  
    # answer에 -1만 추가해줍니다.
    if cnt == 0 :
        answer.append(-1)
    answer.sort()
    return answer

arr = list(map(int,input('숫자 리스트 입력: ').split()))
div = int(input('나눌 숫자 입력: '))

print(solution(arr,div))