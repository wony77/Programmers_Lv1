# Programmers_Lv1 약수의 개수와 덧셈
def solution(left, right):
    cnt = 0
    sum = 0
    for i in range(left,right+1):
        for j in range(1,i+1):
            if i % j == 0:
                cnt+=1
        if cnt % 2 == 0:
            sum+=i
        else:
            sum-=i
        cnt = 0
    answer = sum
    return answer

left, right = map(int,input().split())
print(solution(left,right))