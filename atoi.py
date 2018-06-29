import re

class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        # get rid of the spaces on the left
        no_space = str.lstrip(" ")
        if not no_space:
            return 0

        # checking format, remember to escape '+' and '.'
        if not re.fullmatch('^[\+-]?\d*\.?\d+.*$', no_space):
            return 0

        # find the number part, note that to find substring we cannot have '^$'
        match = re.search('[\+-]?(\d*)(\.?)(\d+)', no_space).group()
        
        # round the number
        match = match.split(".")[0]
        if not match:
            return 0
        
        # trivial part for this question
        try:
            match = int(match)
            if match > (2**31)-1: match = (2**31)-1
            elif match < (-2**31): match = -2**31

        except:
            match = -2**31 if match[0] == '-' else (2**31)-1

        return match

    # optimization
    def myAtoi_2(self, str):
        """
        :type str: str
        :rtype: int
        """
        no_space = str.lstrip(" ")
        if not no_space:
            return 0

        # note the '^' means the first n words (head part) of the full string must conform to the expression
        match = re.search('^[\+-]?(\d*)(\.?)(\d+)', no_space)
        
        if not match:
            return 0
        
        match = match.group().split(".")[0]
        if not match:
            return 0
        
        try:
            match = int(match)
            if match > (2**31)-1: match = (2**31)-1
            elif match < (-2**31): match = -2**31

        except:
            match = -2**31 if match[0] == '-' else (2**31)-1

        return match
