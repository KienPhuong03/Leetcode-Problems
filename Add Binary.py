### Problem: Given two binary strings a and b, return their sum as a binary string.
#Example 1:

#Input: a = "11", b = "1"
#Output: "100"
#Example 2:

#Input: a = "1010", b = "1011"
#Output: "10101"
 
# Constraints:
# 1 <= a.length, b.length <= 104
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.

#MY CODE
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        rem = 0
        output = ""
        if len(a) < len(b):
            return self.addBinary(b, a)
        else:
            ix = 0
            while ix < len(a):
                if ix <= len(b) - 1:
                    current_sum = int(a[len(a) - 1 - ix]) + int(b[len(b) - 1 - ix]) + rem
                else:
                    current_sum = int(a[len(a) - 1 - ix]) + rem
                if current_sum < 2:
                    output = str(current_sum) + output
                    rem = 0
                else:
                    rem = 1
                    output = str(current_sum % 2) + output
                ix += 1
            if rem == 1:
                output = "1" + output
            return output
        

#Other solution:
