#K번째 수 찾는 프로그램
def solution(array, commands):
    array1 = []
    answer = []

    #commands 를 com으로 for문을 돌리면 [[1],[2]] << 리스트가 [1] [2] << 이렇게 하나씩 반복해줍니다. 
    for com in commands:
        #받아온 A리스트를 B[0][i] B[0][j] 로 잘라서 담아줍니다.
        array1 = array[com[0]-1:com[1]]
        #정렬을 하고
        array1.sort()
        #정렬 된 수 중 K번째 수를 정답에 담아줍니다.
        answer.append(array1[com[2]-1])
    
    return answer


#위의 함수를 실행하기위에 만든 임시..

# i ~ j 까지 끊고 k번째 수를 뽑아라 라는 변수를 B리스트에 추가할 때 cnt를 1씩 올려
# 추가하는 방법.
cnt = 0
#긴 리스트가 있어야함.. 이거 잘라서 테스트 할거에요.
A = [2,8,6,4,3,1,9]
B = []

#i ~ j 까지 끊고 k번째 수를 뽑아라 라는 변수를 B리스트에 추가
while(True):
    i = int(input())
    j = int(input())
    k = int(input())
    s = input("더 입력하십니까(Y|N): ")
    B.append([])
    B[cnt].append(i)
    B[cnt].append(j)
    B[cnt].append(k)
    
    if s == 'N':
        break
    cnt+=1

print(solution(A,B))