class Solution:
    def myAtoi(self, s):
        INT_MIN = -2**31     
        INT_MAX = 2**31 - 1   
        
        s = s.lstrip()
        
        if not s:  
            return 0
        
        sign = 1
        index = 0
        
        if s[0] == '-':
            sign = -1
            index = 1
        elif s[0] == '+':
            index = 1
        
        result = 0
        
        while index < len(s):
            if not s[index].isdigit():
                break
            
            digit = int(s[index])
            
            if result > INT_MAX // 10 or (result == INT_MAX // 10 and digit > 7):
                return INT_MIN if sign == -1 else INT_MAX
            
            result = result * 10 + digit
            index += 1
        
        return result * sign