import sys
import math

class Node(object):
    counter=0
    def __init__(self,c):
        self.ch=c
        self.branch={}
        self.counter=0

class Trie(object):
    def __init__(self):
        self.stone=Node('^')
        
    def insert(self, word):
        data=list(word)
        self.insertRecurively(self.stone, data)
        
    def insertRecurively(self, node, data):
        if len(data)>0:
            if data[0] not in node.branch:
                node.branch[data[0]]=Node(data[0])
            node.branch[data[0]].counter+=1
            self.insertRecurively(node.branch[data[0]],data[1:])

class Solution:
    def check(self, ch: str, node:Node, depth:int)-> int:
        if ch in node.branch:
            freq=node.branch[ch].counter
            if freq >= 3:
                return self.check(ch, node.branch[ch], depth+1)
        return depth-1
        
    def maximumLength(self, s: str) -> int:
        trie=Trie()
        n=len(s)
        for i in range(n):
            trie.insert(s[i:])
        result=-1
        for ch in "abcdefghijklmnopqrstuvwxyz":
            if ch in trie.stone.branch:
                result=max(result,self.check(ch, trie.stone,1))
        return -1 if result <= 0 else result

sln=Solution()
assert -1==sln.maximumLength(s = "abcdef")
assert 2==sln.maximumLength(s = "aaaa")
assert 1==sln.maximumLength(s = "abcaba")