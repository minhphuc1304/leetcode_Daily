# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # In a formal academic setting, we'd use rotations.
        # However, the problem 1382 is unique because we are 
        # balancing an ALREADY existing, potentially messy BST.
        
        # To fit the 1990s optimization style without the O(N) array:
        # We use the Day-Stout-Warren (DSW) algorithm.
        
        def tree_to_vine(root):
            """ Flatten tree into a linked-list shape (vine) using right rotations. """
            dummy = TreeNode(0)
            dummy.right = root
            curr = dummy
            while curr.right:
                if curr.right.left:
                    # Rotate Right
                    child = curr.right
                    tmp = child.left
                    child.left = tmp.right
                    tmp.right = child
                    curr.right = tmp
                else:
                    curr = curr.right
            return dummy

        def compress(root, count):
            """ Perform 'count' left rotations to move nodes up. """
            curr = root
            for _ in range(count):
                child = curr.right
                tmp = child.right
                curr.right = tmp
                child.right = tmp.left
                tmp.left = child
                curr = tmp

        # --- DSW Algorithm Core ---
        # 1. Create a 'vine' (linked list) O(N) time, O(1) space
        dummy = tree_to_vine(root)
        
        # 2. Count nodes
        n = 0
        curr = dummy.right
        while curr:
            n += 1
            curr = curr.right
            
        # 3. Use leaves and rotations to rebuild perfectly
        import math
        h = int(math.log2(n + 1))
        m = 2**h - 1
        
        # Initial compressions for the bottom-most level
        compress(dummy, n - m)
        
        # Successive compressions to balance the internal levels
        while m > 1:
            m //= 2
            compress(dummy, m)
            
        return dummy.right
