from typing import List

class Solution:
        
    # 定義循環位移矩陣函數
    def cyclic_shift(self, mat, k):
        # 獲取矩陣的行數和列數
        rows, cols = len(mat), len(mat[0]) if mat else 0

        # 對每一行進行循環位移
        for i in range(rows):
            # 如果是偶數索引行，向左循環位移 k 次，否則向右循環位移 k 次
            if i % 2 == 0:
                # 偶數索引行向左循環位移
                mat[i] = mat[i][k % cols:] + mat[i][:k % cols]
            else:
                # 奇數索引行向右循環位移
                mat[i] = mat[i][-k % cols:] + mat[i][:-k % cols]

        return mat

    # 定義檢查矩陣是否在循環位移後恢復原狀的函數
    def areSimilar(self, original_mat: List[List[int]], k: int)-> bool:
        # 復制原始矩陣，以便進行循環位移操作
        mat_copy = [row[:] for row in original_mat]
        
        # 對復制的矩陣進行循環位移
        shifted_mat = self.cyclic_shift(mat_copy, k)
        
        # 檢查位移後的矩陣是否與原始矩陣相同
        return shifted_mat == original_mat

sln=Solution()
assert False==sln.areSimilar([[1,2]], k = 1)     
assert True==sln.areSimilar( [[2,2],[2,2]], k = 3)     
assert True==sln.areSimilar( [[1,2,1,2],[5,5,5,5],[6,3,6,3]], k = 2)        