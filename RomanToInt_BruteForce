class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict={
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        x=list(s)
        num=0
        flagged=0
        i=0
        while i < len(x)-1:
            if x[i] == "I" and x[i+1] == "V":
                num+=4
                if i+1 == len(x)-1:
                    flagged=1
                i+=2
            elif x[i] == "I" and x[i+1] == "X":
                num+=9
                if i+1 == len(x)-1:
                    flagged=1
                i+=2
            elif x[i] == "X" and x[i+1] == "L":
                num+=40
                if i+1 == len(x)-1:
                    flagged=1
                i+=2
            elif x[i] == "X" and x[i+1] == "C":
                num+=90
                if i+1 == len(x)-1:
                    flagged=1
                i+=2
            elif x[i] == "C" and x[i+1] == "D":
                num+=400
                if i+1 == len(x)-1:
                    flagged=1
                i+=2
            elif x[i] == "C" and x[i+1] == "M":
                num+=900
                if i+1 == len(x)-1:
                    flagged=1
                i+=2
            else:
                num+=roman_dict[x[i]]
                i+=1
        if flagged == 0:
            num+=roman_dict[x[-1]]
        return num
        