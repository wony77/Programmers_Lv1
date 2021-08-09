# Programmers_Lv1 크레인 인형뽑기
# https://programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):
    buket = []
    answer = []
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                buket.append(board[j][i-1])
                board[j][i-1] = 0
                if buket[-1:] == buket[-2:-1]:
                    answer += buket[-2:-1]
                    buket = buket[:-2]
                break
    
    return len(answer)*2

board = [[0,0,0,0,0],
         [0,0,1,0,3],
         [0,2,5,0,1],
         [4,2,4,4,2],
         [3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

print(solution(board,moves))