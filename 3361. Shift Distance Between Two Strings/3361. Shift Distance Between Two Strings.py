from typing import List

class Solution:
    def shiftDistance(self, s: str, t: str, nextCost: List[int], previousCost: List[int]) -> int:
        total_cost = 0
        
        for i in range(len(s)):
            if s[i] == t[i]:
                continue
                
            src = ord(s[i]) - ord('a')  # 源字符的索引
            dst = ord(t[i]) - ord('a')  # 目標字符的索引
            
            # 計算向前移動的成本
            forward_cost = 0
            curr = src
            while curr != dst:
                forward_cost += nextCost[curr]
                curr = (curr + 1) % 26
            
            # 計算向後移動的成本
            backward_cost = 0
            curr = src
            while curr != dst:
                backward_cost += previousCost[curr]                
                curr = (curr - 1) % 26

            
            # 選擇最小成本
            total_cost += min(forward_cost, backward_cost)
            
        return total_cost
    
sln=Solution()
assert 31==sln.shiftDistance( s = "leet", t = "code", nextCost = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], previousCost = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
assert 2==sln.shiftDistance(s = "abab", t = "baba", nextCost = [100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], previousCost = [1,100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])