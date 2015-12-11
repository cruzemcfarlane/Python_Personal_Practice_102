def make_empty_tree():
    return ('btree',[])

def makeTree(root,left,right):
    return ('btree',[root,left,right])

def root(tree):
    return tree[1][0]

def left_subtree(tree):
    return tree[1][1]

def right_subtree(tree):
    return tree[1][2]

def is_tree_empty(tree):
    return tree==('btree',[])

def is_btree(tree):
    return type(tree)==type(()) and type(tree[1])==type([]) and len(tree)==2 and tree[0]=='btree'

def is_leaf_tree(tree):
    return not is_tree_empty(tree) and is_tree_empty(left_subtree(tree)) and is_tree_empty(right_subtree(tree))==0

def preorder(tree):
    if tree==():
        return []
    else:
        return root(tree)+preorder(left_subtree(tree))+preorder(right_subtree(tree))

def inorder(tree):
    if tree==[]:
        return []
    else:
        return inorder(left_subtree(tree))+[root(tree)]+inorder(right_subtree(tree))

def postorder(tree):
    if is_tree_empty(tree)==True:
        return []
    else:
        return postorder(left_subtree(tree))+postorder(right_subtree(tree))+[root(tree)]

tr=[7,[5,[],[]],[11,[9,[],[]],[]]]
