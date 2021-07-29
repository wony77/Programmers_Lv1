# Programmers_Lv1 소수 만들기

def solution(nums):
    answer =0
    sum, cnt = 0 , 0
    # i는 nums의 배열 크기만큼 돌린다.
    for i in range(0,len(nums)):
        # j는 i보다 항상 1계단 높은 크기 만큼 반복한다.
        for j in range(i+1,len(nums)):
            # k는 j보다 항상 1계단 높은 크기 만큼 반복한다. 
            for k in range(j+1,len(nums)):
                #sum이라는 변수에 중복되지 않은 3개의 수를 넣는다.
                sum = nums[i] + nums[j] + nums[k]
                # sum의 크기만큼 반복한다. 소수 판별을 위한 것
                for l in range(1,sum):
                    # 만약 sum이 l로 나누어 떨어지면 카운트를 올려준다.
                    if sum % l == 0:
                        cnt += 1
                    # 카운트가 2 이상이면 약수가 나 자신을 포함에 더 있는것이므로 
                    # 카운트를 초기화하고 반복문을 멈춰준다. 계속 돌리면 효율성이 떨어짐.
                    if cnt >= 2 :
                        cnt = 0
                        break
                # 카운트가 1이 라는것은 약수에 1만 있고 자기자신을 나누면 0으로 떨어지는 
                # 소수라는 뜻입니다. 그러므로 카운트가 1인것은 소수이므로 
                # answer에 +1을 해주고 카운트를 초기화 해줍니다.
                if cnt == 1:
                    answer += 1
                    cnt = 0
    return answer

number = list(map(int,input('숫자 입력: ').split()))
print(solution(number))