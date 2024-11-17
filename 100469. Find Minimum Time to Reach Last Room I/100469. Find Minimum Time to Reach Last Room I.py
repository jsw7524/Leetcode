from typing import List

import heapq
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n=len(moveTime)
        m=len(moveTime[0])
        arrivedTime=[ [ (10**9)+1 for j in range(m)] for i in range(n)]
        queue = [(0, (0,0))]
        visited = {}
        while len(queue) > 0:
            current_distance, current_node = heapq.heappop(queue)
            if current_node in visited:
                continue    
            visited[current_node]=current_distance
            if current_node == (n-1, m-1):
                 return current_distance              
            currentY , currentX = current_node
            if currentY+1 < n and (currentY+1, currentX) not in visited:
                heapq.heappush(queue,(max(current_distance+1,1+moveTime[currentY+1][currentX]),(currentY+1, currentX)))
            if currentY-1 >= 0 and (currentY-1, currentX) not in visited:
                heapq.heappush(queue,(max(current_distance+1,1+moveTime[currentY-1][currentX]),(currentY-1, currentX)))
            if currentX+1 < m and (currentY, currentX+1) not in visited:
                heapq.heappush(queue,(max(current_distance+1,1+moveTime[currentY][currentX+1]),(currentY, currentX+1)))
            if currentX-1 >= 0 and (currentY, currentX-1) not in visited:
                heapq.heappush(queue,(max(current_distance+1,1+moveTime[currentY][currentX-1]),(currentY, currentX-1)))
        return -1
    
sln=Solution()

assert 60==sln.minTimeToReach(moveTime = [[15,58],[67,4]])


# assert 3==sln.minTimeToReach(moveTime = [[0,1],[1,2]])
# assert 6==sln.minTimeToReach(moveTime = [[0,4],[4,4]])
# assert 3==sln.minTimeToReach(moveTime = [[0,0,0],[0,0,0]])

