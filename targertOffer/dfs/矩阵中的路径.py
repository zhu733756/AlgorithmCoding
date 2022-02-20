# 给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。

# https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if word == "":
            return True

        directions = [(1,0),(-1,0),(0,-1),(0,1)]

        def dfs(r, c, m, n, index, length):
            if index == length:
                return True
                
            if r<0 or r >= m  or c < 0 or c >= n or board[r][c] == "." or word[index] != board[r][c]:
                return False

            val = board[r][c]

            board[r][c] = "."

            for dx,dy in directions:
                x,y = r+dx, c+dy
                if dfs(x, y, m, n, index+1,length):
                    return True

            board[r][c] = val

            return False

        m,n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and dfs(i,j,m,n,0,len(word)):
                    return True

        return False