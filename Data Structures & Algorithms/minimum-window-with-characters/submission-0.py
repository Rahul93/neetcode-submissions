class Solution:
    def minWindow(self, s: str, t: str) -> str:
        map = defaultdict(int)

        for ch in t:
            map[ch] += 1

        start, end, head, count, diff = 0, 0, 0, len(t), float("inf")

        while end < len(s):
            if map[s[end]] > 0:
                count -= 1
            
            map[s[end]] -= 1
            end += 1

            while count == 0:
                if end - start < diff:
                    diff = end - start
                    head = start

                map[s[start]] += 1

                if map[s[start]] > 0:
                    count += 1
                start += 1

        return s[head:head + diff] if diff != float("inf") else ""