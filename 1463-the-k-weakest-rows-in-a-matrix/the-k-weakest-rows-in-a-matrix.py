class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        ROWS, COLS = len(mat), len(mat[0])
        rows = []
        for row in range(ROWS):
            ones = 0
            for col in range(COLS):
                if mat[row][col] == 1:
                    ones +=1
                else:
                    break
            rows.append([ones,row])

        rows.sort()
        return [rows[i][1] for i in range(k)]


            
        