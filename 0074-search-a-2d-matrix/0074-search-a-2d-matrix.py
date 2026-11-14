class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        ROWS,COLS=len(matrix),len(matrix[0])
        l,r=0,ROWS*COLS-1
        while l<=r:
            m=int((l+r)/2)
            row=m//COLS
            col=m%COLS
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]<target:
                l=m+1
            else:
                r=m-1
        return False