'''This program constructs a tree from a pre order and post order traversal of a n-ary tree
'''
pre = [5,6,1,3,2,7,10,9,11]
post = [3,1,2,6,7,9,11,10,5]
visited = []

class Tree(object):
    def __init__(self,val):
        self.val = val
        self.child = []
    def __str__(self):
        for c in self.child:
            print  c
        return str(self.val)

def createTree(pre):
    if not pre:
        return None
    root = Tree(pre[0])
    pre_len = len(pre)
    i=1
    if pre_len == 1:
            return root
    while i< pre_len:
        count = find_child(pre[i]) + 1
        child = createTree(pre[i:i+count])
        root.child.append(child)
        i += count
    return root
        
def find_child(node):
    if node in visited:
        return 0
    visited.append(node)
    i = 0
    for i in range(len(post)):
        if node == post[i]:
            break
    
    j = 0
    i -= 1
    while i>= 0:
        if post[i] in visited:
            break
        j += 1
        i -= 1
    return j
    
print createTree(pre)
