import collections


class IMMUNIZATION:
    # init class
    def __init__(self, vaccineList, edges):
        self.vaccineList = vaccineList
        self.edges = edges
        self.nodes = []
        self.adj_list = {}

    # Read Input file and create the respective vertices, edges and nodes
    def readInputfile(self, inputfile):
        file = open(inputfile)
        # read the file as a list
        for line in file:
            vaccineList.append(line.strip().split('/'))
        # creating a edges matrix from the list
        for vaccine in vaccineList:
            for x in range(len(vaccine) - 1):
                edges.append([vaccine[0].strip(), vaccine[x + 1].strip()])
        # creating vertices from the list
        for vaccine in vaccineList:
            for x in range(len(vaccine)):
                if vaccine[x] in self.nodes:
                    continue
                else:
                    self.nodes.append(vaccine[x].strip())

    def displayAll(self):
        # opening output file in write mode
        file = open("outputPS16.txt","w")
        file.writelines("--------Function displayAll--------\n")
        # finiding unique strains
        strainList = []
        for vaccine in vaccineList:
            strainList.append(vaccine[0])
        uniqueVaccines = []
        # finiding unique Vaccines
        for vaccine in vaccineList:
            for x in range(1,len(vaccine)):
                if vaccine[x] in uniqueVaccines:
                    continue
                else:
                    uniqueVaccines.append(vaccine[x])
        # writing the output to the file
        file.writelines("Total no. of strains: " + str(len(strainList)) +"\n")
        file.writelines("Total no. of vaccines: " + str(len(uniqueVaccines)) + "\n")
        file.writelines("List of strains: \n")
        for strain in strainList:
            file.writelines(strain +" \n")
        file.writelines("List of Vaccines: \n")
        for vac in uniqueVaccines:
            file.writelines(vac.strip()+ " \n")
        file.writelines("\n")

    # adding  nodes to the adjacency_list
    def add_node(self):
        for node in self.nodes:
            self.adj_list[node] = []

    # adding edges to the adjacency_list
    def add_edge(self, v, e):
        self.adj_list[v].append(e)
        self.adj_list[e].append(v)

    # creating the adjacency_list
    def graph(self):
        self.add_node()
        for edge in edges:
            self.add_edge(edge[0], edge[1])

    # print adjacency list
    def print_adj(self):
        for node in self.nodes:
            print(node, ":", self.adj_list[node])

    # function to display strain for a vaccine
    def displayStrains(self, vaccine):
        try:
            list = self.adj_list[vaccine]
        except:
            list=[]
        file = open("outputPS16.txt", "a")
        file.writelines("--------Function displayStrain --------\n")
        file.writelines("Vaccine name: "+ vaccine +"\n")
        file.writelines("List of Strains: \n")
        if len(list) ==0:
            file.writelines("No Strain Found\n")
        for strain in list:
            file.writelines(strain +" \n")
        file.writelines("\n")

    # function to display vaccines for a strain
    def displayVaccine(self, strain):
        file = open("outputPS16.txt","a")
        try:
            list = self.adj_list[strain]
        except:
            list=[]
        file.writelines("--------Function displayVaccine --------\n")
        file.writelines("Strain name: " + strain + "\n")
        file.writelines("List of Vaccine: \n")
        if len(list) == 0:
            file.writelines("No Vaccine Found \n")
        for strain in list:
            file.writelines(strain + " \n")
        file.writelines("\n")

    #bfs algorithm
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

    # bfs with shortest path
    def bfs_sp(self, start, goal):
        explored = []
        # Queue for traversing the
        queue = [[start]]
        # If the desired node is
        # reached
        if start == goal:
            print("Same Node")
            return
        # Loop to traverse the graph
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
                        ("Shortest path = ", *new_path)
                        return
                explored.append(node)
        return

vaccineList = []  # list containing vaccine and strains
edges = []  # matrix of edges/associations
immunization = IMMUNIZATION(vaccineList, edges)
immunization.readInputfile("inputPS16.txt")
immunization.displayAll()
immunization.graph()
immunization.displayStrains("CoviShied")
immunization.displayVaccine("229E")
immunization.bfs_sp("Covaxin","CoviShild")
immunization.bfs("Covaxin")