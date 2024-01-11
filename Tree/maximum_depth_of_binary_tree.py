import collections
#DFS
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
    

#BFS
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root: return 0
        q = collections.deque([root])
        res = 0

        while q:
            tmp = collections.deque()
            for node in q:
                if node.left: tmp.append(node.left)
                if node.right: tmp.append(node.right)
            q = tmp
            res += 1
        return res
    
# Time complexity : O(n)
# Space complexity : O(n)