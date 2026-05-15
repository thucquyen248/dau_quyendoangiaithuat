class Solution:
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])
        heights = [0] * (n + 1)
        max_area = 0

        for row in matrix:
            for j in range(n):
                if row[j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0

            stack = []
            for i, h in enumerate(heights):
                while stack and heights[stack[-1]] > h:
                    height = heights[stack.pop()]
                    width = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, height * width)
                stack.append(i)

        return max_area