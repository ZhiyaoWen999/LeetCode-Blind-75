#DFS
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if not p or not q:
            return False
        
        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            

#BFS
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        queue = deque()
        queue.append(p)
        queue.append(q)
        while queue:
            p = queue.pop()
            q = queue.pop()
            if not p and not q:
                continue
            if (not p or not q) or p.val != q.val:
                return False

            queue.append(p.left)
            queue.append(q.left)
            queue.append(p.right)
            queue.append(q.right)
            
        return True
    

# Time complexity : O(min(n, m))
# Space complexity : O(min(n, m))