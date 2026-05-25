class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        traingle=[]
        for row in range(rowIndex+1):
            current_row=[1]*(row+1)
            for j in range(1,row):
                current_row[j]=traingle[row-1][j-1]+traingle[row-1][j]
            traingle.append(current_row)
        return traingle[rowIndex]
        