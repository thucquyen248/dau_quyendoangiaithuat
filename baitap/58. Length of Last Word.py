class Solution:
    def lengthOfLastWord(self, s):
        i = len(s) - 1
        # Bỏ khoảng trắng cuối
        while i >= 0 and s[i] == ' ':
            i -= 1
        length = 0
        # Đếm độ dài từ cuối đến khi gặp khoảng trắng
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1
        return length