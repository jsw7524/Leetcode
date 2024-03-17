from typing import List

class Node(object):
    counter=0
    def __init__(self,c):
        self.ch=c
        self.branch={}
        Node.counter+=1

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
            self.insertRecurively(node.branch[data[0]],data[1:])
            
    def query(self, word):
        data=list(word)
        return self.queryRecurively(self.stone, data)       

    def queryRecurively(self, node, data):
        if len(data)>0:
            if data[0] in node.branch:
                return 1 + self.queryRecurively(node.branch[data[0]],data[1:])
        return 0

class Solution:
    
    def check(self, arr: List[str], query:str):
        pass
            
        
    
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        pass
        
        