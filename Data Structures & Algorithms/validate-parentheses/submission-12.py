class Solution:
    def isValid(self, s: str) -> bool:
        dict1={')':'(',"}":"{","]":"["}
        stk=[]
        for i in s:
            if i in "[({":
                stk.append(i)
            else:
                if stk and stk[-1]==dict1[i]:
                    stk.pop()
                else:
                    return False
        return True if not stk else False
        
            