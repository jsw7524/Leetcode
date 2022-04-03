import sys
import math

class Node(object):
    counter=0
    def __init__(self,c):
        self.ch=c
        self.branch={}
        Node.counter+=1

class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stone=Node('^')
        
    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        data=list(word)
        self.insertRecurively(self.stone, data)
        
    def insertRecurively(self, node, data):
        if len(data)>0:
            if data[0] not in node.branch:
                node.branch[data[0]]=Node(data[0])
            self.insertRecurively(node.branch[data[0]],data[1:])

#use example
# trie=Trie()
# n = int(input())
# for i in range(n):
#     telephone = input()
#     trie.insert(telephone)