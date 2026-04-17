class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        bottom, top = 0, rows - 1
        
        while bottom <= top:
            row = (bottom + top) // 2

            if target > matrix[row][-1]:
                bottom = row + 1   # FIXED
            elif target < matrix[row][0]:
                top = row - 1      # FIXED
            else:
                break

        if bottom > top:   # FIXED
            return False

        row = (bottom + top) // 2

        l, r = 0, cols - 1

        while l <= r:
            mid = (l + r) // 2

            if matrix[row][mid] < target:
                l = mid + 1
            elif matrix[row][mid] > target:
                r = mid - 1
            else:
                return True

        return False