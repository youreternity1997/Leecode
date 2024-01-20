class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows<=1:
            return s
        zigzag = ['' for i in range(numRows)]
        row, step = 0, 1
        
        for crct in s:
            zigzag[row] += crct

            if row == 0:
                step = 1
            elif row == numRows-1:
                step = -1
            
            row += step

        return ''.join(zigzag)

if __name__ == '__main__':
    s = "PAYPALISHIRING"
    numRows = 3
    ans = Solution().convert(s, numRows)
    print('ans=', ans)