def build_graph(adjList):
    # 如果是空的，直接回傳 None
    if not adjList:
        return None

    # 先建立所有節點 (index 0→節點1，index 1→節點2，以此類推)
    n = len(adjList)
    nodes = [Node(i+1) for i in range(n)]
    
    # 依照 adjList，幫每個節點加上對應的鄰居
    for i, neighbors in enumerate(adjList):
        for nei_val in neighbors:
            # 節點的標號是從1開始，所以 nei_val-1 對應陣列的 index
            nodes[i].neighbors.append(nodes[nei_val - 1])
    
    # 回傳第一個節點 (通常預設從節點1作為整個圖的起點)
    return nodes[0]

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        mapping = {}        # 用於將「原節點的值」對應到「新複製的節點」
        stack = [node]      # DFS 所使用的堆疊，初始只放入傳入的起始節點
        
        while stack:
            curr = stack.pop()
            print("curr===", curr)
            
            # 如果尚未為 curr 建立複製節點，就在 mapping 裡面先加一個
            if curr.val not in mapping:
                mapping[curr.val] = Node(curr.val)
            
            # 為 curr 的每個鄰居進行處理
            for neighbor in curr.neighbors:
                # 如果這個鄰居還沒有被複製，立即建立並推入 stack
                if neighbor.val not in mapping:
                    mapping[neighbor.val] = Node(neighbor.val)
                    stack.append(neighbor)
                
                # 把「鄰居的複製節點」加入到「當前複製節點」的 neighbors
                mapping[curr.val].neighbors.append(mapping[neighbor.val])
        
        # 回傳最初輸入 node 對應的「複製節點」
        return mapping[node.val]

input = [[2,4],[1,3],[2,4],[1,3]]
start_node = build_graph(input)

s = Solution()
ans = s.cloneGraph(start_node)
print('ans =', ans)