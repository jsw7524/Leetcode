class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        result=[0] * (n+1)
        x, y = (x, y) if y > x else (y, x) 
        for i in range(1,n+1):
            for j in range(i+1,n+1):
                dis=min(abs(x-i) + (1 if x!=y else 0) + abs(j-y),   abs(i-j)  )
                # 4 cases
                # if i <= x <= y <= j:
                #     dis = min(abs(x-i) + (1 if x!=y else 0) + abs(j-y),   abs(i-j)  )
                # elif i <= x <= j <=y:
                #     dis = min(abs(x-i) + (1 if x!=y else 0) + abs(j-y),   abs(i-j)  )
                # elif x <= i <= y <=j:
                #     dis = min(abs(x-i) + (1 if x!=y else 0) + abs(j-y),   abs(i-j)  )
                # else:
                #     dis = min(abs(x-i) + (1 if x!=y else 0) + abs(j-y),   abs(i-j)  )
                #     #dis= abs(i-j)
                result[dis]+=2
        return result[1:]