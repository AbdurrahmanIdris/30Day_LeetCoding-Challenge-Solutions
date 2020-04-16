"""
Problem statement:
Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. 
We define the validity of a string by these rules:
##Any left parenthesis '(' must have a corresponding right parenthesis ')'.
##Any right parenthesis ')' must have a corresponding left parenthesis '('.
##Left parenthesis '(' must go before the corresponding right parenthesis ')'.
##'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.

Example 1:
Input: "()"
Output: True
Example 2:
Input: "(*)"
Output: True
Example 3:
Input: "(*))"
Output: True
"""
## Note: To be honest: I tried to solve it a lot but I couldn't reach. So I get hints from the solution in the solution tab of the main
## leet code problem -> Greedy Algorithm. Then I wrote it in my style. 

class Solution:
    def checkValidString(self, s: str) -> bool:
        low , high = 0, 0
        
        """
        low represent the lowest probability number of open brackets
        high represent the highest probability number of open bracket
        If we encounter '(' both low and high will increase by 1
        and If we encounter ')' both should decrease by 1
        but if we encounter '*' then it may be an open bracket or a closed bracket or none of them
        but we will consider only the best and worst cases of '*' which are closed or open respectively.
        if we consider it '(' then highest will increase by 1 and if ')' then lowest will decrease by 1.
        """
        
        for char in s:
            if char == '(':
                low += 1
                high += 1
            elif char == ')':
                low -= 1
                high -= 1
            else:
                low -= 1
                high += 1
            """    
            if high equals -1 we should break the loop and return false because this means the number of
            close brackets exceeds the number of open ones.
            """
            if high < 0:
                return False
            """    
            After checking the variable high, now we are sure that high isn't below 0 so if low is below zero
            we will reset its value, i.e. we will use some of the asterisks as an open bracket ;))
            """
            low = max(low,0)
        return low == 0
