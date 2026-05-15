class Solution:
    def compareVersion(self, version1, version2):
        v1 = list(map(int, version1.split(".")))
        v2 = list(map(int, version2.split(".")))
        n = max(len(v1), len(v2))
        for i in range(n):
            r1 = v1[i] if i < len(v1) else 0
            r2 = v2[i] if i < len(v2) else 0
            if r1 < r2:
                return -1
            elif r1 > r2:
                return 1
        return 0
