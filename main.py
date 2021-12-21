import collections


class IMMUNIZATION:
    def __init__(self, vaccineList, edges):
        self.vaccineList = vaccineList
        self.edges = edges
        self.nodes = []
        self.adj_list = {}

    def readInputfile(self, inputfile):
        file = open(inputfile)
        for line in file:
            vaccineList.append(line.strip().split('/'))
        for vaccine in vaccineList:
            for x in range(len(vaccine) - 1):
                edges.append([vaccine[0].strip(), vaccine[x + 1].strip()])
        for vaccine in vaccineList:
            for x in range(len(vaccine)):
                if vaccine[x] in self.nodes:
                    continue
                else:
                    self.nodes.append(vaccine[x].strip())

    def displayAll(self):
        file = open("outputPS16.txt","w")
        file.writelines("--------Function displayAll--------\n")
        strainList = []
        for vaccine in vaccineList:
            strainList.append(vaccine[0])
        uniqueVaccines = []
        for vaccine in vaccineList:
            for x in range(1,len(vaccine)):
                if vaccine[x] in uniqueVaccines:
                    continue
                else:
                    uniqueVaccines.append(vaccine[x])
        file.writelines("Total no. of strains: " + str(len(strainList)) +"\n")
        file.writelines("Total no. of vaccines: " + str(len(uniqueVaccines)) + "\n")
        file.writelines("List of strains: \n")
        for strain in strainList:
            file.writelines(strain +" \n")
        file.writelines("List of Vaccines: \n")
        for vac in uniqueVaccines:
            file.writelines(vac.strip()+ " \n")

    def add_node(self):
        for node in self.nodes:
            self.adj_list[node] = []

    def add_edge(self, v, e):
        self.adj_list[v].append(e)
        self.adj_list[e].append(v)

    def graph(self):
        self.add_node()
        for edge in edges:
            self.add_edge(edge[0], edge[1])


    def displayStrains(self, vaccine):
        print(self.adj_list[vaccine])

    def print_adj(self):
        for node in self.nodes:
            print(node, ":", self.adj_list[node])

    def displayVaccine(self, strain):
        print(self.adj_list[strain])

    def bfs(self,root):
        visited, queue = set(), collections.deque([root])
        visited.add(root)
        while queue:
            # Dequeue a vertex from queue
            vertex = queue.popleft()
            print(str(vertex) + " ", end="")
            # If not visited, mark it as visited, and
            # enqueue it
            for neighbour in self.adj_list[vertex]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)

        # Use BFS to check path between s and d

    def isReachable(self, s, d):
        # Mark all the vertices as not visited
        visited = [False] * (self.nodes)
        # Create a queue for BFS
        queue = []
        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True
        while queue:
            # Dequeue a vertex from queue
            n = queue.pop(0)
            # If this adjacent node is the destination node,
            # then return true
            if n == d:
                return True
        #  Else, continue to do BFS
        for i in self.adj_list[n]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True
        # If BFS is complete without visited d
        return False


    def BFS_SP(self, start, goal):
        explored = []

        # Queue for traversing the
        # graph in the BFS
        queue = [[start]]

        # If the desired node is
        # reached
        if start == goal:
            print("Same Node")
            return

        # Loop to traverse the graph
        # with the help of the queue
        while queue:
            path = queue.pop(0)
            node = path[-1]

            # Condition to check if the
            # current node is not visited
            if node not in explored:
                neighbours = self.adj_list[node]

                # Loop to iterate over the
                # neighbours of the node
                for neighbour in neighbours:
                    new_path = list(path)
                    new_path.append(neighbour)
                    queue.append(new_path)

                    # Condition to check if the
                    # neighbour node is the goal
                    if neighbour == goal:
                        print("Shortest path = ", *new_path)
                        return
                explored.append(node)

        # Condition when the nodes
        # are not connected
        print("So sorry, but a connecting" \
              "path doesn't exist :(")
        return

vaccineList = []  # list containing vaccine and strains
edges = []  # matrix of edges/associations
graph = IMMUNIZATION(vaccineList, edges)
graph.readInputfile("inputPS16.txt")
graph.displayAll()
print(graph.edges)
graph.graph()
graph.print_adj()
graph.displayStrains("CoviShield")
graph.displayVaccine("229E")
graph.isReachable("Covaxin","CoviShield")
