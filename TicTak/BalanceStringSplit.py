class Solution:
    def balancedStringSplit(self, s: str) -> int:
        index=count=0
        for x in s:
            if x == 'L':
                index+=1
            if x == 'R':
                index-=1
            if index==0:
                count+=1
        return count        
