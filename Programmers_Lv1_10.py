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
print(solution(abs,sign))
<<<<<<< HEAD

# 다른 방식의 풀이 
def solution(absolutes, signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))
# 해석 
# for absolutes, sign in zip(absolutes, signs) for 문을 한번에 여러개 돌리겠다는  zip함수 이용
# ex) [4, 7, 12] [true, false, true] -> 4,true ... 12,true 
# absolutes, sign << 에 위의 순서대로 하나씩 할당되어줍니다.
# if sign: < 이것은 만약 sign == True 일때 동작 하겠다는 의미이고, 
# True 일때 sum 함수를 통해 absolutes를 더하고 False일때는 -absolutes를 더하라는 의미 입니다.
# 해석 끝~
=======
>>>>>>> 1dfc145a6e78c4dd847c193ab5adf77604e849bf
