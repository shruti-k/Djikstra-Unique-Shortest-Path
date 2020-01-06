#DO NOT CHANGE ANY EXISTING CODE IN THIS FILE
class Dijkstra:
    weight = []
    usp = []
    pq = []
    s = []
    def Dijkstra_alg(self, n, e, mat, s):
         #Write your code here to calculate shortest paths and usp values from source to all vertices
		 #This method will have four inputs (Please see testcase file)
		 #This method should return a two dimensional array as output (Please see testcase file)
        #Initialization
        #weight is a list of distances of each node from the source
        weight = [float('inf') for i in range(n+1)]
        weight[s] = 0
        self.weight = weight
        ans = []
        usp = [1 for i in range(n+1)]
        self.usp = usp
        pq = []
        for v,w in enumerate(self.weight):
            if(v!=0):
                pq.append([v,w])
        self.pq = pq
        #Calls build_min_heap to create a priority queue
        self.build_min_heap()
   
        
        while(len(self.pq)>0):
            #Extracts the node with minimum weight from the queue
            u = self.extract_min()
            #Calls relax function for all unvisited ajdacent nodes of u
            for e in mat:
                if e[0]==u[0] and e[1] not in self.s:
                    weight_rel = self.relax(u[0],e[1],e[2])
            
                elif e[1]==u[0] and e[1] not in self.s:
                    weight_rel = self.relax(u[0],e[0],e[2])
        #prints result as a list of lists
        res = []
        for i in range(1,n+1):
            res.append([self.weight[i],self.usp[i]])
        return res
                
    def relax(self,u,v,edge):
        if(self.weight[v] > self.weight[u] + edge):
            self.decrease_key(v,self.weight[v],self.weight[u] + edge)
            self.weight[v] = self.weight[u] + edge
            self.usp[v] = self.usp[u]
        #usp of node becomes 0 if multiple shortest paths to source exist
        elif(self.weight[v] == self.weight[u] + edge):
            self.usp[v] = 0
        
    def parent(self,i):
        return (i - 1)//2
     
    def left(self,i):
        return 2*i + 1
     
    def right(self,i):
        return 2*i + 2
     
    def build_min_heap(self):
        length = len(self.pq)
        start = self.parent(length - 1)
        while start >= 0:
            self.min_heapify(index=start, size=length)
            start = start - 1
     
    def min_heapify(self,index,size):
        
        l = self.left(index)
        r = self.right(index)

        if (l < size) and (self.pq[l][1] < self.pq[index][1]):
                smallest = l
                
        else:
                smallest = index
                
        if (r < size) and (self.pq[r][1] < self.pq[smallest][1]):
            smallest = r
        if (smallest != index):
            self.pq[smallest], self.pq[index] = self.pq[index], self.pq[smallest]
            self.min_heapify(smallest, size)
            
    def extract_min(self):
        u = self.pq.pop(0)
        self.s.append(u)
        if(len(self.pq)!=0):
            last = self.pq.pop(len(self.pq)-1)
            self.pq.insert(0,last)
            self.min_heapify(0,len(self.pq))
        return u
        
    def decrease_key(self,vertex,old_value,new_value):
        ind = self.pq.index([vertex,old_value])
        self.pq[ind] = ([vertex,new_value])
        par = self.parent(ind)
        child = ind
        while(par>=0):
            if self.pq[child][1] < self.pq[par][1]:
                self.pq[child],self.pq[par] = self.pq[par],self.pq[child]
                child = par
                par = self.parent(child)
            else:
                break
