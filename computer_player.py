import pygame
from positions import *
from draw import *
import queue

def analyze(my_board, next_player, x, y):  # phân tích bàn cờ nếu như thêm vào vị trí (x, y)
    board = coppyList(my_board)
    board[x][y] = next_player
    if have_five(board, next_player, x, y):
        return 1e18
    board[x][y] = -next_player
    if have_five(board, -next_player, x, y):
        return 1e18
    board[x][y] = next_player
    pointAttack = 0
    pointAttack = max(pointAttack, four_in_a_row(board, next_player, x, y, '1'))
    pointAttack = max(pointAttack, three_in_a_row(board, next_player, x, y, '1'))
    pointAttack = max(pointAttack, two_in_a_row(board, next_player, x, y, '1'))
    board[x][y] = -next_player
    pointDefense = 0
    pointDefense = max(pointDefense, four_in_a_row(board, next_player * -1,x , y, '2'))
    pointDefense = max(pointDefense, three_in_a_row(board, next_player * -1, x, y, '2'))
    pointDefense = max(pointDefense, two_in_a_row(board, next_player * -1,x, y, '2'))
    # if( pointAttack > pointDefense ):
    #     return pointAttack
    # else:
    #     return -pointDefense
    return pointAttack + pointDefense

def analyze_current_move(table, next_player):  # phần để chạy được
    point, position_x, position_y = 0, 0, 0
    ntable = len(table)
    for x in range(ntable):
        for y in range(ntable):
            if table[x][y] == 0:
                cur_point = analyze(table, next_player, x, y)
                if point < cur_point:
                    point = cur_point
                    position_x = x
                    position_y = y
    return (point, position_x, position_y)

def deep_analyze(board, xx, yy):  
    q = queue.Queue()
    table = coppyList(board)
    q.put((table, 0, -1, 0, 0, 0)) # table, dept, next_player, x, y, result
    answer = (-1e18, 0, 0) # point, x, y
    while q.qsize() > 0 :
        container = q.get()
        list = coppyList(container[0])
        dept = container[1]
        nxt = container[2]
        x , y = container[3], container[4]
        result = container[5]
        # print("dept = ", dept, ' ', x, ' ', y, ' ', result)
        # if dept >= 2 :print(dept)
        if dept >= 2:
            # print(result)
            if result > answer[0]:
                # print(x, ' ', y)
                answer = (result, x, y)
            continue
        nlist = len(list)
        if dept % 2 == 1 :
            new_l = coppyList(list)
            answer = (0, 0, 0)
            answer = max(answer, enemy_four_in_a_row(new_l, 1 , x , y))
            answer = max(answer, enemy_three_in_a_row(new_l, 1, x , y))
            answer = max(answer, enemy_two_in_a_row(new_l, 1, x , y))
            new_l[answer[1]][answer[2]] = 1
            if dept == 0 :
                q.put((new_l, dept + 1, -1, answer[1], answer[2], result - answer[0]))
            else :
                q.put((new_l, dept + 1, -1, x, y, result - answer[0]))
            continue

        for i in range(max(0, xx - n), min(len(board), xx + n)):
            for j in range(max(0, yy - n), min(len(board), yy + n)):
                if list[i][j] == 0:
                    point = analyze(list, nxt, i, j)
                    new_list = coppyList(list)
                    new_result = result
                    if dept % 2 == 0:
                        new_result += point
                        new_list[i][j] = -1
                    else:
                        new_result -= point
                        new_list[i][j] = 1
                    if dept == 0:
                        q.put((new_list, dept + 1, -nxt, i, j, new_result))
                    else:
                        q.put((new_list, dept + 1, -nxt, i, j, new_result))
    return answer


def max_value(board, alpha, beta, depth, x, y):
    if depth == 0:
        return analyze(board, 1, x, y)
    v = -1e18
    for i in range(max(0, x - n), min(len(board), x + n)):
        for j in range(max(0, y - n), min(len(board), y + n)):
            if board[i][j] == 0:
                board[i][j] = 1
                v = max(v, min_value(board, alpha, beta, depth - 1, i, j))
                board[i][j] = 0
                if v >= beta:
                    return v
                alpha = max(alpha, v)
    return v

def min_value(board, alpha, beta, depth, x, y):
    if depth == 0:
        return analyze(board, -1, x, y)
    v = 1e18
    for i in range(max(0, x - n), min(len(board), x + n)):
        for j in range(max(0, y - n), min(len(board), y + n)):
            if board[i][j] == 0:
                board[i][j] = -1
                v = min(v, max_value(board, alpha, beta, depth - 1, i, j))
                board[i][j] = 0
                if v <= alpha:
                    return v
                beta = min(beta, v)
    return v

def deep_analyze_2(board, xx, yy):
    alpha = -1e18
    beta = 1e18
    point, position_x, position_y = 0, 0, 0
    ntable = len(board)
    for i in range( xx ,max(0, xx - 5),  -1):
        for j in range( yy-1, max(0, yy - 5), -1):
            if board[i][j] == 0:
                board[i][j] = -1
                cur_point = max_value(board, alpha, beta, dosau, i, j)
                board[i][j] = 0
                if point > cur_point:
                    point = cur_point
                    position_x = i
                    position_y = j
        for j in range( yy , min(len(board), yy + 5)):
            if board[i][j] == 0:
                board[i][j] = -1
                cur_point = max_value(board, alpha, beta, dosau, i, j)
                board[i][j] = 0
                if point > cur_point:
                    point = cur_point
                    position_x = i
                    position_y = j
                    
    for i in range(xx, min(len(board), xx + 5)):
        for j in range( yy + 1 , min(len(board), yy + 5)):
            if board[i][j] == 0:
                board[i][j] = -1
                cur_point = max_value(board, alpha, beta, dosau, i, j)
                board[i][j] = 0
                if point > cur_point:
                    point = cur_point
                    position_x = i
                    position_y = j
        for j in range( yy, max(0, yy - 5), -1):
            if board[i][j] == 0:
                board[i][j] = -1
                cur_point = max_value(board, alpha, beta, dosau, i, j)
                board[i][j] = 0
                if point > cur_point:
                    point = cur_point
                    position_x = i
                    position_y = j

    return (point, position_x, position_y)

board = new_board()
board[2][2] = 1
# board[2][3] = -1
# board[2][4] = 1
# board[1][3] = -1
# board[3][3] = 1
for i in range(len(board)):
    for j in range(len(board)):
        print(board[i][j], end = " ")
    print()
for i in range(len(board)):
    for j in range(len(board)):
        if board[i][j] == 0:
            board[i][j] = -1
            print(max_value(board, -1e18, 1e18, 2, i, j), end = " ")
            board[i][j] = 0
    print()


# screen: màn hình hiện đang chơi, board: mảng 2 chiều thể hiện trạng thái của bàn cờ
def computer_reply(screen, board, xx, yy):
    # tìm nước đi của máy
    # board: mảng 2 chiều thể hiện trạng thái của bàn cờ
    # return: screen mới cùng board mới
    # -1 : O   ;   1 : X
    # position = analyze_current_move(board, -1)
    position = deep_analyze(board, xx, yy)
    # position = deep_analyze_2(board, xx, yy)
    drawO(screen, position[1], position[2])
    board[position[1]][position[2]] = -1
    pass
