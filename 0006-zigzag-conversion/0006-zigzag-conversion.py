class Solution:
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        
        rows = [[] for _ in range(numRows)]
        period = 2 * (numRows - 1) 
        
        for i, char in enumerate(s):
            pos = i % period
            
            if pos < numRows:
                row = pos
            else:
                row = period - pos
            
            rows[row].append(char)
        
        result = ""
        for row in rows:
            result += "".join(row)
        
        return result