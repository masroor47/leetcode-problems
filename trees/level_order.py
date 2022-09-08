from tree import TreeNode


def level_order(root):
    if not root:
        return []
    queue = [[root]]
    res = []
    while queue:
        # level is a list of the current level's nodes
        level = queue.pop(0)
        lvl = []
        while level:
            curr = level.pop(0)
            lvl.append(curr.val)
            if not queue:
                queue.append([])
            if curr.left:
                queue[0].append(curr.left)
            if curr.right:
                queue[0].append(curr.right)
        if lvl:
            print(f"done adding to lvl: {lvl}")
            res.append(lvl)
    return res
    



test_l = TreeNode(9)
test_r_l = TreeNode(15)
test_r_r = TreeNode(7)
test_r = TreeNode(20, test_r_l, test_r_r)
test1 = TreeNode(3, test_l, test_r)
print(level_order(test1))