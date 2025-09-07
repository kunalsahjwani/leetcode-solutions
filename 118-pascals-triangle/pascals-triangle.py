
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Initialize output with the first row of Pascal's triangle
        output = [[1]]
        for i in range(numRows - 1):
            temp = [0] + output[-1] + [0]
            row = []

            for j in range(len(output[-1]) + 1):
                val = temp[j] + temp[j+1]
                print(val)
                print(temp[j], temp[j+1])
                row.append(val)
                
            print(row)
            output.append(row)
        return output




        