class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        fmt = 'TreeNode(data={}, left={}, right={})'
        return fmt.format(self.data, self.left, self.right)


class BinarySearchTree:
    def __init__(self, tree_data):
        self._root = TreeNode(tree_data[0])
        for elem in tree_data[1:]:
            self._insert(self._root, elem)
    
    def _insert(self, node, elem):
        if node is None:
            node = TreeNode(elem)
        else:
            if int(node.data) < int(elem):
                if node.right is None:
                    node.right = TreeNode(elem, None, None)
                else:
                    self._insert(node.right, elem)
            else:
                if node.left is None:
                    node.left = TreeNode(elem, None, None)
                else:
                    self._insert(node.left, elem)


    def data(self):
        return self._root

    def sorted_data(self):
        ret = []
        self._traverse(self._root, ret)
        return ret

    def _traverse(self, node, ret):
        if node.left is not None:
            self._traverse(node.left, ret)
        ret.append(node.data)
        if node.right is not None:
            self._traverse(node.right, ret)
