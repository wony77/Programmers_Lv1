# Programmers_Lv1 비밀지도

def solution(n,arr1,arr2):
    # n*n 사각형 만들기
    map0 = []
    map1 = []
    map2 = []
    answer1 = [[0]*n for i in range(n)]
    answer0 = [[0]*n for i in range(n)]
    answer = [[0]*n for i in range(n)]

    # 2진수 변환 작업
    for ar1,an1 in zip(arr1,answer1):
        ar1 = bin(ar1)
        ar1 = ar1[2:].zfill(n)
        for i in range(n):
            an1[i] = ar1[i]
        map1.append(an1)
        
    for ar2,an0 in zip(arr2,answer0):
        ar2 = bin(ar2)
        ar2 = ar2[2:].zfill(n)
        for i in range(n):
            an0[i] = ar2[i]
        map2.append(an0)
    
    for i in range(0,n):
        for j in range(0,n):
            if map1[i][j] == '0' and map2[i][j] == '0':
                answer[i][j] = '0'
            else:
                answer[i][j] = '#'
    
    for m in answer:
        map0.append("".join(m).replace('0',' '))
    return map0

n = int(input('n * n 정사각형을 만드려고 합니다. n의 크기는?: '))
arr1 = list(map(int,input('지도 1의 모양: ').split()))
arr2 = list(map(int,input('지도 2의 모양: ').split()))

print(solution(n,arr1,arr2))