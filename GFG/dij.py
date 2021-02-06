from collections import defaultdict
class RoutingGraph:
    def minDistance(self,d,my_queue):
        minimum = float("Inf")
        min_index = -1
        for i in range(len(d)):
            if d[i] < minimum and i in my_queue:
                minimum = d[i]
                min_index = i
        return min_index
    
    def printPath(self, parent, j):
        if parent[j] == -1:
            print (j)
            return
        self.printPath(parent , parent[j])
        print (j)
    
    def printSolution(self, d, parent):
        src = self.src
        print("Vertex \t\t\nSrc -> Des\tNext_Hop\tDistance\tPath")
        for i in range(1, len(d)):
            print("\n%d --> %d \t%d\t" % (src, i, d[i]),end="")
            if(d[i]!=float('inf')):
                temp_path = []
                temp_path_string = ""
                currentNode = i
                hop_count=0
                while(currentNode != src and currentNode >= 0 ):
                    hop_count+=1
                    temp_path.insert(0,currentNode)
                    temp_path_string = str(currentNode) + " ->" +  temp_path_string
                    currentNode = parent[currentNode]
                if(i == src):
                    temp_path.insert(0,src)
                temp_path_string = str(src)+"->"+temp_path_string 
                temp_path_string = temp_path_string[:-2]
                print(f"\tNextHop:{temp_path[0]}\t",d[i],"\t\t",temp_path_string,"\t\tTotal_Hops: ",hop_count)
    def dijkstra(self, graph, src):
        self.src = src
        row = len(graph)
        col = len(graph[0])
        d = [float("Inf")] * row
        parent = [-1] * row
        d[src] = 0
        my_queue = []
        for i in range(row):
            my_queue.append(i)
        while my_queue:
            u = self.minDistance(d,my_queue)
            my_queue.remove(u)
            for i in range(col):
                if graph[u][i] and i in my_queue:
                    if d[u] + graph[u][i] < d[i]:
                        d[i] = d[u] + graph[u][i]
                        parent[i] = u
        self.printSolution(d,parent)

g= RoutingGraph()

network_graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
        ]
src = int(input("Enter the source node :"))
g.dijkstra(network_graph,src)