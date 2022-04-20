def solution(board, moves):
    answer = 0
    st = []
    for i in range(len(moves)):
        check = moves[i] - 1;
        for j in range(len(board)):
            if board[j][check] != 0:
                if len(st) != 0 and st[-1] == board[j][check]:
                    st.pop(-1)
                    answer += 2
                else:
                    st.append(board[j][check])
                board[j][check] = 0
                break
    return answer