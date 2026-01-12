from collections import deque
def max_depth(root):
    if not root:
        return 0
    q=deque([root])
    level=0
    
    while q:
        for _ in range(len(q)):
            node=q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        level+=1
    return level
