class Solution(object):
    def romanToInt(self,s):
        bang = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        ket_qua = 0
        for i in range(len(s)):
            if i + 1 < len(s) and bang[s[i]] < bang [s[i+1]]:
                ket_qua -= bang[s[i]]
            else:
                ket_qua += bang[s[i]]
        return ket_qua