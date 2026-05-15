class Solution:
    def fullJustify(self, words, maxWidth):
        res = []
        i = 0
        n = len(words)

        while i < n:
            line_len = len(words[i])
            j = i + 1
            while j < n and line_len + 1 + len(words[j]) <= maxWidth:
                line_len += 1 + len(words[j])
                j += 1

            line_words = words[i:j]
            spaces = maxWidth - sum(len(w) for w in line_words)

            if j == n or len(line_words) == 1:
                line = " ".join(line_words)
                line += " " * (maxWidth - len(line))
            else:
                gaps = len(line_words) - 1
                space_per_gap = spaces // gaps
                extra = spaces % gaps

                line = ""
                for k in range(gaps):
                    line += line_words[k]
                    line += " " * (space_per_gap + (1 if k < extra else 0))
                line += line_words[-1]

            res.append(line)
            i = j

        return res