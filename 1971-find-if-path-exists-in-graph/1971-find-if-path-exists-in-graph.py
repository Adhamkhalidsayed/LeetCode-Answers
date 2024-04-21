class Solution:
    
    def dfs (self, node, graph, vis, destination):
        if node == destination:
            return True
        
        vis[node] = True
        
        for neighbor in graph[node]:
            if  vis[neighbor] == False:
                if self.dfs(neighbor, graph, vis, destination):
                    return True
        return False
                
    
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        
        for s, d in edges:
            graph[s].append(d)
            graph[d].append(s)
        
        vis = [False]*n
        
        return self.dfs(source, graph, vis, destination)