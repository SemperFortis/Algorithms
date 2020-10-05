queue = []
visited = []

class Node:
    # children is a list of nodes 
    def __init__(self, current, children):
        self.current = current
        self.children = children
    
    def find_children(self):
        if len(self.children) > 0:
            for child in self.children:
                if self.current not in queue:
                    queue.append(child)

        for node in queue:
            if node.current not in visited:
                visited.append(node.current)
                queue.pop(0)
                node.find_children()


graph = Node(5, [Node(7, [Node(3, []), Node(10, [Node(14, []), Node(11, [])])]), Node(9, [Node(2, []), Node(1, [])])])
graph.find_children()

print(visited)