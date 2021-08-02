# Programmers_Lv1 내적
# https://programmers.co.kr/learn/courses/30/lessons/70128

# a와 b의 내적은 a[0]*b[0] + a[1]*b[1] + ... + a[n-1]*b[n-1] 입니다. (n은 a, b의 길이)
def solution(a, b):
    answer = 0
    # 내적은 배열의 길이가 같으므로 zip을 통해 하나로 묶고 
    # 원소를 하나씩 가져와 곱한 후 answer에 더해주면 됩니다.
    for a1, b1 in zip(a,b):
        answer += (a1*b1)
    return answer

a = list(map(int,input('a의 정수 배열: ').split()))
b = list(map(int,input('b의 정수 배열: ').split()))

print(solution(a,b))