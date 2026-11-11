# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def dfs(node):
            if not node:
                return [True, 0]

            left_balance,left_height = dfs(node.left)
            right_balance,right_height = dfs(node.right)

            is_balanced = left_balance and right_balance and abs(left_height - right_height) <= 1
            height = 1 + max(left_height, right_height)

            return [is_balanced, height]

        return dfs(root)[0]
            
        