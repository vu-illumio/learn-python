class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def treeInOrderTraversal(node):
    if node is None:
        return None
    else:
        treeInOrderTraversal(node.left)
        print(f'{node.data}', end=',')
        treeInOrderTraversal(node.right)

def treeSearch(node, data):
    if node is None:
        return False
    elif node.data == data:
        return True
    elif node.data > data:
        return treeSearch(node.left, data)
    else:
        return treeSearch(node.right, data)

def treeInsert(node, data):
    if node is None:
        return Node(data)
    elif node.data == data:
        raise Exception('[Error] tree insertion of duplicate data is not allowed')
    if node.data > data:
        node.left = treeInsert(node.left, data)
    else:
        node.right = treeInsert(node.right, data)
    return node

def treeMinValue(node):
    if node is None:
        raise Exception('[Error] tree is empty')
    while node.left is not None:
        node = node.left
    return node

def treeDelete(node, data):
    if node is None:
        raise Exception('[Error] tree node data is not found')
    if node.data > data:
        node.left = treeDelete(node.left, data)
    elif node.data < data:
        node.right = treeDelete(node.right, data)
    else:
        if node.left is None:
            child = node.right
            del node
            return child
        elif node.right is None:
            child = node.left
            del node
            return child
        else:
            node.data = treeMinValue(node.right).data
            node.right = treeDelete(node.right, node.data)
    return node
  
