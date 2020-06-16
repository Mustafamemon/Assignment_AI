import queue as Q

heuristics_table = {
    'Arad' :366,'Mehadia':241,
    'Bucharest':0,'Neamt':234,
    'Craiova':160,'Oradea':380,
    'Drobeta':242,'Pitesti':100,
    'Eforie':161,'Rimnicu Vilcea':193,
    'Fagaras':176,'Sibiu':253,
    'Giurgiu':77,'Timisoara':329,
    'Hirsova':151,'Urziceni':80,
    'Iasi':226,'Vaslui':199,
    'Lugoj':244,'Zerind':374,
}


node = ['Arad' ,'Mehadia','Bucharest','Neamt','Craiova','Oradea',
    'Drobeta','Pitesti','Eforie','Rimnicu Vilcea','Fagaras','Sibiu',
    'Giurgiu','Timisoara','Hirsova','Urziceni','Iasi','Vaslui','Lugoj','Zerind']

def fucn(c,r):
    if c == r:
        return float('inf')
    else:
        return 0
    
graph ={r : { c : fucn(c,r) for c in node} for r in node}

graph['Arad']['Zerind'] = 75
graph['Arad']['Timisoara'] = 118
graph['Arad']['Sibiu'] = 140

graph['Mehadia']['Lugoj'] = 70
graph['Mehadia']['Drobeta'] = 75

graph['Bucharest']['Urziceni'] = 85
graph['Bucharest']['Pitesti'] = 101
graph['Bucharest']['Giurgiu'] = 90
graph['Bucharest']['Fagaras'] = 211

graph['Neamt']['Iasi'] = 87

graph['Craiova']['Rimnicu Vilcea'] = 146
graph['Craiova']['Pitesti'] = 138
graph['Craiova']['Drobeta'] = 120

graph['Oradea']['Zerind'] = 71
graph['Oradea']['Sibiu'] = 151

graph['Drobeta']['Mehadia'] = 75
graph['Drobeta']['Craiova'] = 120

graph['Pitesti']['Rimnicu Vilcea'] = 97 
graph['Pitesti']['Craiova'] = 138
graph['Pitesti']['Bucharest'] = 101

graph['Eforie']['Hirsova'] = 86

graph['Rimnicu Vilcea']['Pitesti'] = 97
graph['Rimnicu Vilcea']['Craiova'] = 146
graph['Rimnicu Vilcea']['Sibiu'] = 80

graph['Fagaras']['Sibiu'] = 99 
graph['Fagaras']['Bucharest'] = 211

graph['Sibiu']['Oradea'] = 151
graph['Sibiu']['Fagaras'] = 99
graph['Sibiu']['Arad'] = 140
graph['Sibiu']['Rimnicu Vilcea'] = 80

graph['Giurgiu']['Bucharest'] = 90

graph['Timisoara']['Arad'] = 118
graph['Timisoara']['Lugoj'] = 111

graph['Hirsova']['Eforie'] = 86
graph['Hirsova']['Urziceni'] = 98

graph['Urziceni']['Hirsova'] = 98
graph['Urziceni']['Vaslui'] = 142
graph['Urziceni']['Bucharest'] = 85

graph['Iasi']['Vaslui'] = 92
graph['Iasi']['Neamt'] = 87

graph['Vaslui']['Iasi'] = 92
graph['Vaslui']['Urziceni'] = 142 

graph['Lugoj']['Timisoara'] = 111
graph['Lugoj']['Mehadia'] = 70 

graph['Zerind']['Oradea'] = 71
graph['Zerind']['Arad'] = 75 

def BFS(start,end):
    bfs = graph
    qu = Q.Queue()
    qu.put((0,None,start)) #(cost,parent,source)
    visited = list()
    actual_path = list()
    parent  = list() 
    total_cost = 0 
    actual_cost = 0

    while qu.empty()==False:
        
        val = qu.get()
        start = val[2] # source or start point
        if(start not in visited): 
            p = val[1] #parent 
            parent.append(p)
            visited.append(start)
            total_cost = total_cost + val[0] #cost
            if(start == end):
                actual_path.append(end)
                p = parent.pop()
                while p is not None:
                    actual_cost = actual_cost + graph[end][p]
                    end = p
                    actual_path.append(p)
                    ind = visited.index(p)
                    p = parent[ind]
                print('\n------------------------Visited Path---------------------------\n')
                print(visited,end=' -> total cost :  ')
                print(total_cost,end='\n\n------------------------Actual Path---------------------------\n\n')
                actual_path.reverse()
                print(actual_path,end=' -> actual cost :  ')
                print(actual_cost)
                return 0
            for j in node:
                if (j not in visited) and (j != start) :
                    try:
                        if(bfs[start][j]!=0 and bfs[start][j]!=float('inf')):
                            qu.put((bfs[start][j],start,j))
                    except KeyError:
                        print('\nSource -> NOT FOUND')
                        return 0
            
    print('\nDestination -> NOT FOUND')
    return 0



def UCS(start,end):
    ucs = graph
    qu = Q.PriorityQueue()
    qu.put((0,None,start))
    visited = list()
    parent  = list()
    actual_path = list()
    total_cost = 0
    actual_cost = 0
    while qu.empty()==False:
        val = qu.get()
        start = val[2]
        if start not in visited:
            p = val[1]
            actual_cost = val[0]
            try:
                total_cost  = total_cost + graph[p][start]
            except KeyError:
                pass
            parent.append(p)
            visited.append(start)
            if(start == end):
                actual_path.append(end)
                p = parent.pop()
                while p is not None:
                    actual_path.append(p)
                    ind = visited.index(p)
                    p = parent[ind]
                print('\n------------------------Visited Path---------------------------\n')
                print(visited,end=' -> total cost :  ')
                print(total_cost,end='\n\n------------------------Actual Path---------------------------\n\n')
                actual_path.reverse()
                print(actual_path,end=' -> actual cost :  ')
                print(actual_cost)
                
                return 0
            for j in node:
                if j not in visited and j != start:
                    try:
                        if(ucs[start][j]!=0 and ucs[start][j]!=float('inf')):
                            if qu.__contains__(j):
                                qu.update(j,actual_cost+ucs[start][j])
                            else:
                                qu.put((actual_cost+ucs[start][j],start,j))
                    except KeyError:
                        print('\nSource -> NOT FOUND')
                        return 0
    print('\nDestination -> NOT FOUND')
    return 0


def GBFS(start,end):
    gbfs = graph
    qu  = Q.PriorityQueue()
    visited  =list()
    visited.append(start)
    parent  = list()
    actual_path = list()
    total_cost = 0
    actual_cost = 0
    parent.append(None)
    while True:
        for j in node:
            # ask teacher about visited check
            if j not in visited and j != start:
                try:
                    if(gbfs[start][j]!=0 and gbfs[start][j]!=float('inf')):
                        if qu.__contains__(j):
                            qu.update(j,heuristics_table[j])
                        else:
                            qu.put((heuristics_table[j],gbfs[start][j],j,start))
                except KeyError:
                    print('\nSource -> NOT FOUND')
                    return 0 
        if qu.empty() == True:
            print('\nDestination -> NOT FOUND')
            return 0
       
        val = qu.get()
        parent.append(val[3])
        total_cost = total_cost + val[1]
        start = val[2]
        visited.append(start)
        if start == end :
            actual_path.append(end)
            p = parent.pop()
            while p is not None:
                actual_cost = actual_cost + graph[end][p]
                end = p
                actual_path.append(p)
                ind = visited.index(p)
                p = parent[ind]
            print('\n------------------------Visited Path---------------------------\n')
            print(visited,end=' -> total cost :  ')
            print(total_cost,end='\n\n------------------------Actual Path---------------------------\n\n')
            actual_path.reverse()
            print(actual_path,end=' -> actual cost :  ')
            print(actual_cost)
            return 0 
        
    return 0


def IDDFS(start,end,maxDepth):
    iddfs   = graph
    stack   = list()
    visited = list()
    parent  = list()
    actual_path = list()
    total_cost  = 0
    actual_cost = 0
    depth   =  0
    stack.append(start)
    visited.append(start)
    parent.append(None)
    curretn_node = None
    while len(stack)!=0:
        curretn_node = None
        while curretn_node != stack[len(stack)-1]:
            curretn_node = stack[len(stack)-1]
            if curretn_node == end:
                stack.clear()
                break 
            if(depth == maxDepth):
                depth = depth - 1
                stack.pop()
            else:
                for j in node:
                    if j not in visited and j != start:
                        try:
                            if(iddfs[curretn_node][j]!=0 and iddfs[curretn_node][j]!=float('inf')):
                                stack.append(j)
                                visited.append(j)
                                parent.append(curretn_node)
                                total_cost  = total_cost + iddfs[curretn_node][j]
                                depth = depth + 1
                                break
                        except KeyError:
                            print('\nSource -> NOT FOUND')
                            return 0 
                             
            if  len(stack) == 0:
                break
        if(len(stack)!=0):
            stack.pop()
            depth = depth -1
    
    if len(visited) == len(node):
        print('\nDestintion -> NOT FOUND')
    
    elif curretn_node != end:
       return IDDFS(start,end,maxDepth +1)
    else:    
        actual_path.append(visited[len(visited)-1])
        p = parent.pop()
        while p is not None:
            actual_cost = actual_cost + iddfs[end][p]
            end = p
            actual_path.append(p)
            ind = visited.index(p)
            p = parent[ind]
            
        print('\n------------------------Visited Path---------------------------\n')
        print(visited,end=' ')
        print('depth -> ',maxDepth,end=' -- ')
        print('total_cost -> ',total_cost)
        
        print('\n------------------------Actual Path---------------------------\n')
        actual_path.reverse()
        print(actual_path,end=' ')
        print('actual_cost -> ',actual_cost)
        
        
    
    return 0


if __name__ == "__main__":
   
    start = input('Enter the start point : ') #source
    end   = input('Enter the   end point : ') #destination
    print('\n********************************************** BFS **********************************************')
    BFS(start,end)
    print('\n********************************************** UCS ***********************************************')
    UCS(start,end)
    print('\n********************************************** GBFS ***********************************************')
    GBFS(start,end)
    print('\n********************************************** IDDFS **********************************************')
    IDDFS(start,end,0)
    print('\n********************************************** THE END **********************************************\n')
    
   
    

