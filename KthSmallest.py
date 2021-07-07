class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        for i in range(len(matrix)-1):
            for j in range(len(matrix)):
                p = i
                q = j
                while(matrix[p][q] > matrix[p+1][0]):
                    matrix[p][q], matrix[p+1][0] = matrix[p+1][0], matrix[p][q]
                    matrix[p+1].sort()
                    if (p < (len(matrix)-2)):
                        p += 1
                        q = 0
        if (k % len(matrix)) == 0:
            x = k//len(matrix)-1
        else:
            x = k//len(matrix)
        y = (k % len(matrix))-1
        return(matrix[x][y])
