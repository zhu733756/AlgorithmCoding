#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
@File    :     word-ladder-ii.py
@Time    :     Sat Oct 09 2021
@Author  :     zhu733756
@Contact :     1079333812@qq.com
Last Modified: Sat Oct 09 2021
Modified By:   zhu733756
@Desc    :     None
@link    :     https://leetcode-cn.com/problems/word-ladder-ii/submissions/
'''

from typing import List
from collections import deque, defaultdict

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        words_set = set(wordList)
        if endWord not in words_set:
            return []

        ans = []
        buckets = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                match = word[:i] + "*" +word[i+1:]
                buckets[match].append(word)
                
        
        visited = set()
        queue = deque([(beginWord,[beginWord])])
        found = False
        while queue:
            line_visited = set()
            size = len(queue)
            while size >0:
                word, path = queue.popleft()
                if word == endWord:
                    ans.append(path[:])
                    found = True

                for i in range(len(word)):
                    match = word[:i] + "*"+ word[i+1:]
                    for next_word in buckets[match]:
                        if next_word not in visited:
                            line_visited.add(next_word)
                            queue.append((next_word,path+[next_word]))
                size -= 1
            visited |= line_visited
            if found:
                break

        return ans

if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    Solution().findLadders(beginWord, endWord, wordList)
    