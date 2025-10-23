class Solution:
    def isPalindrome(self, x: int) -> bool:
    #    using string solution
       stringx = str(x)
       return stringx == stringx[::-1]

    #    forward = x
    #    reverse = 0
    #    if x == 0:
    #     True #0 is always a palindrom

    #    while x > 0:
    #     lastdigit = x%10
    #     reverse = reverse * 10 + lastdigit
    #     x = x//10

    #    return forward == reverse
       
        