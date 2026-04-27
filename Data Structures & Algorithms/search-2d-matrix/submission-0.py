class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R , C = len(matrix) , len(matrix[0])
        l ,r = 0 , R*C-1
        while l <= r:
            m = l + ((r-l) // 2)
            row, colu = m//C , m %C 
            if target > matrix[row][colu]:
                l += 1
            elif target < matrix[row][colu]:
                r -= 1
            else:
                return True
        return False
        