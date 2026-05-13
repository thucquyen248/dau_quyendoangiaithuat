class Solution(object):
    def intToRoman(self,num):
        gia_tri = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        ky_hieu = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        ket_qua = ""
        for i in range(len(gia_tri)):
            while num >= gia_tri[i]:
                ket_qua += ky_hieu[i]
                num -= gia_tri[i]
        return ket_qua