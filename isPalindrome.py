import math
def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """

    if x < 0:
        return False
    if x < 10:
        return True

    digits = math.floor(log10(x))+1
    past = 0
    left = right = x

    while (past <= digits//2):
        # left_c is the left-most digit in the left part
        # if left is 234 then left_c = 234 // 100 = 2 in the first loop
        # left then becomes 234 - 2*100 = 34
        # left_div: if left is 234, then left_div is 200, 
        #           if left is 34, then left_div is 30, so it is for getting the left-most digit
        left_div = 10**(digits-past-1)
        left_c   = left  // left_div
        left     = left  -  left_c * left_div

        right_c  = right %  10
        right    = right // 10
        past     = past  +  1

        if left_c != right_c:
            return False
    return True
