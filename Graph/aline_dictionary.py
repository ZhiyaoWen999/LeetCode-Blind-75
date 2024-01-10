import collections
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        indegrees = collections.defaultdict()
        adj = collections.defaultdict(set)
        for word in words:
            for c in word:
                if c in indegrees:
                    continue
                indegrees[c] = 0

        for pre, cur in zip(words, words[1:]):
            for p, c in zip(pre, cur):
                if p != c:
                    if c not in adj[p]:
                        adj[p].add(c)
                        indegrees[c] += 1
                    break
            else:
                # check if the second word is none
                if len(cur) < len(pre):
                    return ""

        res = []
        q = collections.deque()

        for k, v in indegrees.items():
            if v == 0:
                q.append(k)
        
        while q:
            cur = q.popleft()
            res.append(cur)

            for c in adj[cur]:
                indegrees[c] -= 1
                if indegrees[c] == 0:
                        q.append(c)
        # if there is cycle, the final numberof char in res will less than indegrees

        return "".join(res) if len(res) == len(indegrees) else ""