post = [ 5, 6, 3, 1, 4, 2, 7 ]
ino =  [ 7, 5, 6, 2, 3, 1, 4 ]
# ino = [2, 1, 3]
# post = [2, 3, 1]
class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
def construct(post, ino):
    if not post or not ino:
        return
    root = Node(post[-1])
    
    idx = ino.index(root.val)
    root.left = construct(post[:idx], ino[:idx])
    root.right = construct(post[idx:len(post)-1], ino[idx+1:])
    return root
    
Tree = construct(post, ino)
