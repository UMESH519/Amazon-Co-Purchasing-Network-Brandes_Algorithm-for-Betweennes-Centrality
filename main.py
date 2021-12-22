from Algorithm import *
import pprint
import csv
class Graph(object): 

     def __init__(self, data=None): 
           self.adj={}  # empty adjacency hash. This will store the node as its key and the value as the successor node   
             
           
     def add_edges(self, edgelist):   #takes list of list where in the inner list element edges with the first element is predecssor and the second is successor
          for e in edgelist: 
            
              (u,v)=e #untupling the nodes from the edges
              
              if u==v:
                  continue
              #the below statments add nodes if they were not present  
              if u not in self.adj:
                  self.adj[u]={} 
              if v not in self.adj: 
                  self.adj[v]={} 

              self.adj[u][v]=1  

     def __str__(self): #function to print the Graph
        return '{}({})'.format(self.__class__.__name__, dict(self.adj))

        

def parse_edges(link):
    with open(link,'r') as myfile:
            k=[]
            for i in myfile:
                i=i[1:-2]
                k.extend(eval(i))
                
            return k
        
    
    

if __name__ == '__main__':

    path1="../data/High_rank_nodes"
    path2="../data/medium_rank_nodes"
    path3="../data/Low_rank_nodes"
    #print(fileparser(path))


    high_edge_list=parse_edges(path1)
    med_edge_list=parse_edges(path2)
    low_edge_list=parse_edges(path3)



    G_example=Graph()
    example_list=[("Alice","Carol"),("Bob","Carol"),("Carol","Dan"),("Carol","Eve"),("Dan","Frank"),("Eve","Frank"),("Frank","Gale")]
    
    G_example.add_edges(example_list) #To verify Algorithm
    print(G_example)
    print(betweenness_centrality(G_example,scaling=False)) #
    #Verify at https://neo4j.com/docs/graph-data-science/current/algorithms/betweenness-centrality/
    

    G_high = Graph()
    G_high.add_edges(high_edge_list)
    
    BW_high=betweenness_centrality(G_high)
    print("The Average Betweenness Centrality for High Rank Products is:",sum(BW_high.values())/len(BW_high))
    
    G_med=Graph()
    G_med.add_edges(med_edge_list)

    BW_med=betweenness_centrality(G_med)
    print("The Average Betweenness Centrality for Medium Rank Products is:",sum(BW_med.values())/len(BW_med))

    G_low=Graph()
    G_low.add_edges(low_edge_list)

    BW_low=betweenness_centrality(G_low)
    print("The Average Betweenness Centrality for Low Rank Products or Popular products is:",sum(BW_low.values())/len(BW_low))

    ratio= (sum(BW_low.values())/len(BW_low))/(sum(BW_high.values())/len(BW_high))
    print("The ratio of BW for Popular Products to Unpopular Products is:",ratio)

    


    


