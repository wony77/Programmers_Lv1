# 가운데 글자 가져오기
def solution(s):
    answer = ''
    # 글자가 홀수 개 일 때 
    if len(s) % 2 == 1:
        # 문자열이 0부터 시작하므로 길이에 -1 해주고 2로 나눈 몫을 번째 글자를 추가합니다.
        answer += s[(len(s)-1)// 2]
    else:
        # 위 처럼 중간에서 시작하고, 범위를 지정하는데 +2를 해준 이유는 
        # +1 을 하면 0-1이되어 0만 나오므로 0-2를 해야 0-1 의 범위가 지정되게 됩니다.
        answer += s[(len(s)-1)// 2 : (len(s)-1)// 2 + 2]

    return answer

str0 = input()
print(solution(str0))