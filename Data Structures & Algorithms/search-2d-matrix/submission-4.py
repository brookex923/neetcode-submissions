class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowl, rowr = 0, len(matrix) -1
        coll, colr = 0, len(matrix[0]) -1
        
        #find what row
        while rowl <= rowr:
            rowm = (rowl + rowr) // 2
            if target < matrix[rowm][0]:
                rowr = rowm -1
            elif target > matrix[rowm][-1]:
                rowl = rowm +1
            else: 
                break  #target is either in this row or doesn't exist
        
        if not (rowl<=rowr):
            return False
        targetrow = (rowl + rowr) // 2
        while coll <= colr:
            colm = (coll + colr) // 2
            if target < matrix[targetrow][colm]:
                colr = colm - 1
            elif target > matrix[targetrow][colm]:
                coll = colm + 1
            else:
                return True
        # colm = 1, target is greater. colr = 3, coll = 2
        # colm = 2, target is smaller. colr = 1 coll = 2

        return False



