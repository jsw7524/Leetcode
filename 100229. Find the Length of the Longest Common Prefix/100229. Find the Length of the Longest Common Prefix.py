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
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        trie = Trie()
        result=0
        for elm in arr1:
            trie.insert(str(elm))
        for elm in arr2:
            result=max(result,trie.query(str(elm)))
        return result
    
sln=Solution()
assert 0==sln.longestCommonPrefix(arr1 = [1,2,3], arr2 = [4,4,4])
assert 3==sln.longestCommonPrefix(arr1 = [1,10,100], arr2 = [1000])