def make_empty_tree():
    return ("btree",[])

def makeTree(root,left,right):
    return [root,left,right]

def root(tree):
    return tree[1][0]

def left_subtree(tree):
    return tree[1][1]

def right_subtree(tree):
    return tree[1][2]

def is_empty_tree(tree):
    return tree[1]==[]

def is_btree(tree):
    return type(tree)==tuple and tree[0]=='btree' and type(tree[1])==list and len(tree)==2

def is_leaf_tree(tree):
    return not is_empty_tree(tree) and is_empty_tree(left_subtree(tree)) and is_empty_tree(right_subtree(tree))

def postorder(t):
    if is_empty_tree(t)==True:
        return make_empty_tree()
    else:
        return [root(t)]+postorder(left_subtree(t))+postorder(right_subtree(t))
