class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows,cols=len(matrix),len(matrix[0])

        top,bottom=0,rows-1

        while top<=bottom:
            mid=(top+bottom)// 2
            if matrix[mid][0]<=target <=matrix[mid][cols-1] :
                l,r=0,cols-1
                while l<=r:
                    m=(l+r)//2
                    if matrix[mid][m]==target :
                        return True
                    if matrix[mid][m]<target:
                        l=m+1
                    else :
                        r=m-1
            if target < matrix[mid][0]:
                bottom=mid-1
            else :
                top=mid+1

        
        return False