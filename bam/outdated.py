
def find(node):
    r = []
    for c in node.children:
        r += find(c)
    if r or node.is_outdated():
        r.append(node)
    return r
