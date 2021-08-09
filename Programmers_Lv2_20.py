# Programmers_lv2 짝지어 제거하기
# https://programmers.co.kr/learn/courses/30/lessons/12973

def solution(s):
    Same = []

    # 문자열을 하나하나 쪼개서 사용합니다.
    for i in s:
        # 만약 Same이라는 리스트가 비워져있다면
        if not Same:
            # 쪼개어진 i를 Same에 넣어줍니다.
            Same.append(i)
        # Same에 문자가 들어있을 경우
        else:
            # Same의 제일 마지막 문자와 i가 같으면
            if Same[-1] == i:
                # Same의 제일 마지막 문자를 빼줍니다.
                Same.pop()
            else:
                # Same의 마지막 문자와 i가 같지 않으면 i를 추가해줍니다.
                Same.append(i)   
                
    # 빈 sequence(스트링 리스트 튜플)은 False 값을 가집니다.
    # if s: -> True일 때(리스트에 value값이 있을때) 동작하고,
    # if not s: -> False 일 때 (리스트가 비어있을 때) 동작합니다.
    # 이것을 활용하여 풀어보도록 하겠습니다.
    if not Same:
        return 1
    else:
        return 0

s = input('문자열 입력해주세요: ')

print(solution(s))
