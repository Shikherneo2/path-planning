# Useful graph functions
# Author -- Shikhar Dev Gupta

# Returns a list of points from the end to the start
def backtrace(parent, start, end):
    path = [end];
    while path[-1] != start:
        path.append(parent[path[-1]]);
    path.reverse();
    return path;

# Breadth First Search on a graph with a given Source and Target
# Graph - list of lists, adjacency list
# Source - the source node to start the search
# Target - the target node to search for
def bfs(graph, source, target):
    queue = [];
    visited = {};
    parent = {};
    
    for node in xrange(len(graph)):
        visited[node] = False;
        parent[node] = None;
    
    queue.append(source);
    while len(queue) != 0:
        current = queue.pop(0);
        if current == target:
            res = backtrace(parent, source, target);
            return res;
        for neighbor in graph[current]:
            if visited[neighbor] == False:
            	visited[neighbor] = True;
                parent[neighbor] = current;
            	queue.append(neighbor);
    return None;
   
