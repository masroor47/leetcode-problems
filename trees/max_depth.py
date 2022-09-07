from operator import le
from turtle import right
from tree import TreeNode


# 
# Given Root of Binary Tree
# Return maximum depth
# 
# 
# 
# 

def max_depth(root) -> int:

    right_depth, left_depth = 0, 0
    if root.left:
        left_depth = max_depth(root.left)
    if root.right:
        right_depth = max_depth(root.right)

    if right_depth > left_depth:
        return right_depth + 1
    else:
        return left_depth + 1



def max_depth_iter(root) -> int:
    if not root:
        return 0

    queue = [root]
    depth = 0

    while queue:
        for i in range(len(queue)):
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        depth += 1

    return depth
