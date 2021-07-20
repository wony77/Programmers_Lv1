# 숫자 문자열과 영단어
def solution(s):

    # 딕셔너리를 만들어 비교할 예정입니다.
    Eng1 = { }
    Eng = ['zero','one','two','three','four','five','six','seven','eight','nine']
    
    # 위 리스트를 대조하여 0~9까지 영어와 숫자를 딕셔너리로 만들어줍니다.
    for i in range(10):
        Eng1[Eng[i]] = i

    answer = ''
    number2 = ''

    # 받은 문자열을 한 자리씩 쪼개 비교합니다.
    for s1 in s:
        # 만약 s1이라는 문자가 숫자이면 answer에 바로 추가해줍니다.
        if s1.isdigit() == True:
            answer += s1
        # 만약 s1에 문자 저장되어있으면,
        elif s1.isalpha() == True:
            # number2라는 변수에 저장을 해줍니다.
            number2 += s1
            # number2가 쌓여 Eng리스트에 똑같은 문자가 있을 때 이 if문이 동작합니다.
            if number2 in Eng:
                # 딕셔너리의 'number2' value값을 문자로 바꾸어 answer에 추가해줍니다.
                answer+=str(Eng1[number2])
                # number2를 다 사용했기 때문에 초기화 해줍니다.
                number2 =''

    return int(answer)

number = input()
print(solution(number))