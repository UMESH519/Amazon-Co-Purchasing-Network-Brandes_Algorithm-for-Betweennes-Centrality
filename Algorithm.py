
def betweenness_centrality(G,scaling=True):
    betweenness = {}
    for i in G.adj.keys():
        betweenness[i]=0
    nodes = G.adj.keys()
    for s in nodes:
        S, P, sigma = shortest_path_accumulation(G, s)  #Step 1
        betweenness = dependency_accumulation(betweenness, S, P, sigma, s) #Step 2
    
    n=len(G.adj)

    if scaling: #To scale the betweenness centrality measure 
        scale= 1 / ((n - 1) * (n - 2))
        for v in betweenness:
            betweenness[v] *= scale
        return betweenness

    return betweenness


#Helper function For Step 1
def shortest_path_accumulation(G, s):  #Step 1 : Shortest Path Accumulation
    S = [] #empty Stack
    P = {} 
    for v in G.adj.keys():
        P[v] = []
    sigma = dict.fromkeys(G.adj, 0.0) 
    D = {}
    sigma[s] = 1.0
    D[s] = 0
    Q = [s]
    while Q:  
        v = Q.pop(0)
        S.append(v)
        Dv = D[v]
        for w in G.adj[v]:
            if w not in D:
                Q.append(w)
                D[w] = Dv + 1
            if D[w] == Dv + 1:  
                sigma[w] += sigma[v]
                P[w].append(v) 
    return S, P, sigma


#Helper function For Step 2
def dependency_accumulation(betweenness, S, P, sigma, s):   #Step 2 Pairwise Dependency Accumulation 
    delta = dict.fromkeys(S, 0)
    while S:
        w = S.pop()
        coeff = (1 + delta[w]) / sigma[w]
        for v in P[w]:
            delta[v] += sigma[v] * coeff
        if w != s:
            betweenness[w] += delta[w]
    return betweenness




