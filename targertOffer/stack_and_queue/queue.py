# 剑指 Offer 09. 用两个栈实现队列
# https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/

# 用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )

class CQueue:
  
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def appendTail(self, value: int) -> None:
        if len(self.stack1) > 0:
            self.stack2.insert(0,value)
        else:
            self.stack1.append(value)

    def deleteHead(self) -> int:
        if len(self.stack1) == 0:
            return -1
        value = self.stack1.pop()
        if len(self.stack2) > 0:
            self.stack1.append(self.stack2.pop())
        return value