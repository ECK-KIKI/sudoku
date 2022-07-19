# -*- coding: utf-8 -*-
from copy import deepcopy
import os


def checkPuzzleComplete(puzzle, b):
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == 0:
                b[0] = row
                b[1] = col
                return True
    return False


# 检查行
def usedInRow(puzzle, row, num):
    for col in range(9):
        if puzzle[row][col] == num:
            return True
    return False


# 检查列
def usedInColumn(puzzle, col, num):
    for row in range(9):
        if puzzle[row][col] == num:
            return True
    return False


# 检查方格
def usedInBox(puzzle, box_start, box_end, num):
    for row in range(3):
        for col in range(3):
            if puzzle[row + box_start][col + box_end] == num:
                return True
    return False


# 数据校验
def isSafe(puzzle, row, col, num):
    return not usedInRow(puzzle, row, num) \
           and not usedInColumn(puzzle, col, num) \
           and not usedInBox(
        puzzle, row - row % 3, col - col % 3, num)


# 解密流程
def backtrack(puzzle):
    b = [0, 0]
    if not checkPuzzleComplete(puzzle, b):
        return True
    b_row = b[0]
    b_col = b[1]
    for num in range(1, 10):
        if isSafe(puzzle, b_row, b_col, num):
            puzzle[b_row][b_col] = num
            if backtrack(puzzle):
                return puzzle
            puzzle[b_row][b_col] = 0
    return False


if __name__ == '__main__':
    with open('数独题目.txt', 'r') as file:
        board = []
        for line in file:
            line = line.strip()
            board.append([])
            for c in line:
                board[-1].append(int(c))
        var = backtrack(deepcopy(board))
        for answer in var:
            for num in answer:
                print(num, end="")
            print("\r")
    os.system("pause")
