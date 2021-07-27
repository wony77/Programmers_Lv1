# Programmers_Lv1 음양더하기
# https://programmers.co.kr/learn/courses/30/lessons/76501

def solution(absolutes,signs):
    answer = 0
    # 양수 음수 판별 방법 

    # 정수 리스트 길이만큼 반복한다.
    for i in range(len(absolutes)):
        # signs[i]가 True일 경우 양수라 바로 더한다.
        # 여기서 문제 이 코드를 바로 넣게 되면 틀렸다는 결과가 나온다.
        # 그 이유는 파라미터가 들어갈때 문자열 'True'가 아닌 
        # 불타입의 True가 들어가기 때문에 ' ' 를 지워줘야 
        # 프로그래머스에서는 정확한 결과가 나오게 된다.
        if signs[i] == 'True':
            answer += absolutes[i]
        # False인 경우 음수이므로 빼준다.
        else:
            answer -= absolutes[i]
    return answer

abs = list(map(int,input('정수를 입력해 주세요: ').split()))
sign = input('음수(False) / 양수(True): ').split()
print(sign)
print(solution(abs,sign))