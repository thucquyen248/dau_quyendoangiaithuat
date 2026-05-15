class Solution:
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False

        mapst = {}
        mapts = {}

        for cs, ct in zip(s, t):
            if cs in mapst:
                if mapst[cs] != ct:
                    return False
            else:
                mapst[cs] = ct

            if ct in mapts:
                if mapts[ct] != cs:
                    return False
            else:
                mapts[ct] = cs

        return True
