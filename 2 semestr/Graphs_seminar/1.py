n=int(input())
start=0
g={}
for i in range(n):
    x,y=map(int, input().split())
    if x in g:
        g[x].append(y)
    else:
        g[x]=[]
        g[x].append(y)
    if y in g:
        g[y].append(x)
    else:
        g[y]=[]
        g[y].append(x)
visited = [False] * len(g)
prev = [None] * len(g)
def dfs(start, visited, prev, g):
    visited[start] = True
    for u in g[start]:
        if not visited[u]:
            prev[u] = start
            dfs(u, visited, prev, g)
    if visited.count(True)==len(g):
        return True
    else:
        return False
print(dfs(start, visited, prev, g))
