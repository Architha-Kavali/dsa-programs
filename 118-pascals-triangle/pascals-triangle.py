class Solution:
    def generate(self, numRows: int):
        triangle = []

        for row in range(numRows):

            current_row = [1] * (row + 1)

            for j in range(1, row):
                current_row[j] = triangle[row - 1][j - 1] + triangle[row - 1][j]

            triangle.append(current_row)

        return triangle