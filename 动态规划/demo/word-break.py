#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
@File    :     word-break.py
@Time    :     Fri Oct 22 2021
@Author  :     zhu733756
@Contact :     1079333812@qq.com
Last Modified: Fri Oct 22 2021
Modified By:   zhu733756
@Desc    :     判断字符串是否可以由字符字符串数组组成
@link    :     https://leetcode-cn.com/problems/word-break/submissions/
'''

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        下标为i之前的字符串存在字典中；
        dp[i] = dp[i] || dp[i - word_len]
        """
        m= len(s)
        dp = [True] + [False] *m
        for i in range(1, m+1):
            for word in wordDict:
                word_len = len(word)
                if i > word_len and s[i-word_len:i] == word:
                    dp[i] = dp[i-word_len] or dp[i]
        return dp[m]


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        import functools
        @functools.lru_cache(None)
        def back_track(s):
            if(not s):
                return True
            res=False
            for i in range(1,len(s)+1):
                if(s[:i] in wordDict):
                    res=back_track(s[i:]) or res
            return res
        return back_track(s)

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 备忘录
        memo = {}
        def breaker(s,cur):
            # 如果已经算过了 直接返回
            if cur in memo: 
                return memo[cur]
            #  拆分完成
            if cur == len(s):
                memo[cur] = True
                return True

            for word in wordDict:
                # 如果当前的单词比剩下的字符串还要长 则不必查了 以防越界
                if len(word) > len(s) - cur:
                    continue
                # 如果下一个单词能成功拆分且按这样拆下去能成功则返回True
                elif s[cur:cur+len(word)] == word and breaker(s,cur + len(word)):
                    memo[cur] = True
                    return True
            # 没有一种情况拆分成功
            memo[cur] = False
            return False

        
        return breaker(s,0)

import collections as c
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 将字典用集合存以便O(1)搜索
        wordSet = set(wordDict)
        # 创建初始只有一个0元素的双端队列
        queue = c.deque([0])

        memo = {}
        # BFS 先把当前的所有拆法都找出来以后 再进行下一步尝试
        while queue:
            # 先进先出
            cur = queue.popleft()

            # 拆分完成
            if cur == len(s) : 
                return True
            
            # 从当前位置开始一个一个试
            for i in range(cur+1 , len(s) + 1):
                # 如果这个index已经添加过了就不再加了
                if i in memo:
                    pass
                elif s[cur:i] in wordSet:  
                    # 把这种当前的拆法记下 
                    memo[i] = True
                    queue.append(i)
        
        return False


if __name__ == '__main__':
    s = "dogs"
    wordDict = ["dog","s","gs"]
    print(Solution().wordBreak(s,wordDict))
    