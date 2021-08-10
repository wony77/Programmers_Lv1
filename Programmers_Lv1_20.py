# Programmers_Lv1 두개 뽑아서 더하기
# https://programmers.co.kr/learn/courses/30/lessons/68644

def solution(numbers):
    answer = []
    numbers.sort()
    sum = 0
    for i in range(len(numbers)-1):
        for j in range(i+1,len(numbers)):
            sum = numbers[i] + numbers[j]
            if sum not in answer:
                answer.append(sum)
    answer.sort()
    return answer

num = list(map(int,input('숫자 열 입력: ').split()))
print(solution(num))