# 프로그래머스 Lv1 신규 아이디 추천
def solution(new_id):
     # 1단계 대문자 소문자로 변환
     new_id = new_id.lower()

     # 2단계 빼기, 밑줄, 마침표를 제외한 문자 삭제
     A = "_- ."
     new_id = ''.join(x for x in new_id if x in A or x.islower()==True or x.isdigit()==True)

     # 3단계 ".." 점이 연속적으로 중복일 때 '.'으로 바꿔줍니다.
     while '..' in new_id:
          new_id = new_id.replace('..','.')

     # 4단계 처음이나 끝에 '.'이 오면 마침표 제거
     if new_id[0] == '.':
          if len(new_id) >= 2:
               new_id = new_id[1:]
          else:
               new_id = "."
          if new_id[-1] == '.':
               new_id = new_id[:-1]

     # 5단계 공백이 있다면 a로 치환
     if new_id == "":
          new_id = 'a'
     
     # 6단계 16 자리 이상이면 15자리로 맞춰주기, 제일 마지막이 . 이면 . 제거
     if len(new_id) >= 16:
          new_id = new_id[0:15]
     while(True):
          if new_id[-1] == '.':
               new_id = new_id[0:-1]
          else:
               break
     # 7단계 new_id 가 2자리 이하이면 길이가 3이 될때까지 a 추가
     while len(new_id) <= 2:
          new_id += new_id[-1]
          
     answer = ''.join(new_id)
     return answer

user_id = input()
print(solution(user_id))
