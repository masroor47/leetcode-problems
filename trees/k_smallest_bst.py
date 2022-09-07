from tree import TreeNode


def k_smallest(root, k):
    # inorder traversal until reach kth element
    def inorder(root):
        nonlocal i
        if root.left:
            left = inorder(root.left)
            if left != None:
                return left
        
        i += 1
        if i == k:
            return root.val
        elif root.right:
            return inorder(root.right)

        return None


    i = 0
    return inorder(root)