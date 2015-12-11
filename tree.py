def makeEmptyTree():
    return ('btree',[])

def makeEmpty():
    return []

def makeTree(rt,left,right):
    return [rt,left,right]

def getTree(btree):
    return btree[1]

def root(btree):
    return btree[0]

def rightSubTree(btree):
    return btree[1]

def leftSubTree(btree):
    return btree[2]

def el(btree):
	if len(btree)==0:
		return []
	else:
		return [root(btree)]+el(leftSubTree(btree))+el(rightSubTree(btree))

