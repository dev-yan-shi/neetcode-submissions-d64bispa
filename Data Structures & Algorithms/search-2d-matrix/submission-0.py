class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i,j = 0, len(matrix)-1
        row = -1
        while i<=j:
            if matrix[i][0] <= target and matrix[i][len(matrix[0])-1] >=target:
                row = i
                break
            elif matrix[j][0] <= target and matrix[j][len(matrix[0])-1] >=target:
                row = j
                break
            else:
                m = i+ (j-i)//2
                if matrix[m][0] <= target and matrix[m][len(matrix[0])-1] >=target:
                    row = m
                    break
                elif matrix[m][0] > target:
                    j = m-1
                else:
                    i = m+1
        if row==-1:
            return False
        for k in range(len(matrix[row])):
            if matrix[row][k] == target:
                return True
        return False
        
    


        