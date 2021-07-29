# Programmers_Lv1 같은 숫자는 싫어
# https://programmers.co.kr/learn/courses/30/lessons/12906

# 효율 테스트 빵점
# def solution(arr):
#     i = 0
#     while (True):
#         if arr[i] == arr[i+1]:
#             arr.pop(i)
#         else: 
#             i += 1
        
#         if i == len(arr) -1 :
#             break 

#     return arr

def solution(arr):
    answer = []
    for i in range(len(arr)):
        if arr[i] != arr[i-1]:
            answer.append(arr[i])
        elif i == 0:
            answer.append(arr[i])
    return answer


number = list(map(int,input('숫자 리스트 입력: ').split()))
print(solution())