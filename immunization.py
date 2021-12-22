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
        self.graph()

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
        file.close()

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
    def displayStrains(self):
        newlist=[]
        file1 = open("promptsPS16.txt","r")
        for line in file1:
            newlist.append(line.strip().split(':'))
        for x in newlist:
            if x[0]=="displayStrains":
                try:
                    list = self.adj_list[x[1].strip()]
                except:
                    list = []
                file = open("outputPS16.txt", "a")
                file.writelines("--------Function displayStrain --------\n")
                file.writelines("Vaccine name: " + x[1].strip() + "\n")
                file.writelines("List of Strains: \n")
                if len(list) == 0:
                    file.writelines("No Strain Found\n")
                for strain in list:
                    file.writelines(strain + " \n")
                file.writelines("\n")
                file.close()
        file1.close()

    # function to display vaccines for a strain
    def displayVaccine(self):
        newlist = []
        file1 = open("promptsPS16.txt", "r")
        for line in file1:
            newlist.append(line.strip().split(':'))
        for x in newlist:
            if x[0]=="listVaccine":
                file = open("outputPS16.txt", "a")
                try:
                    list = self.adj_list[x[1].strip()]
                except:
                    list = []
                file.writelines("--------Function displayVaccine --------\n")
                file.writelines("Strain name: " + x[1].strip() + "\n")
                file.writelines("List of Vaccine: \n")
                if len(list) == 0:
                    file.writelines("No Vaccine Found \n")
                for strain in list:
                    file.writelines(strain + " \n")
                file.writelines("\n")
                file.close()
        file1.close()

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
                        return new_path
                explored.append(node)
        return

    # function to fina a common strain
    def commonStrain(self):
        newlist = []
        file1 = open("promptsPS16.txt", "r")
        for line in file1:
            newlist.append(line.strip().split(':'))
        for x in newlist:
            if x[0] == "commonStrain":
                vacA = x[1].strip()
                vacB = x[2].strip()
                file = open("outputPS16.txt", "a")
                try:
                    list = self.bfs_sp(vacA, vacB)
                except:
                    list = []
                file.writelines("--------Function Common Strain --------\n")
                file.writelines("Vaccine A " + vacA + "\n")
                file.writelines("Vaccine A " + vacB + "\n")
                if not list:
                    file.writelines("No Common Strain Found \n")
                    file.writelines("\n")
                    continue
                if len(list) > 3:
                    file.writelines("No Common Strain Found \n")
                    file.writelines("\n")
                    continue
                file.writelines("common strain: Yes " + list[1] + " \n")
                file.writelines("\n")
                file.close()
        file1.close()


    #function find vaccine via connecting a vaccine
    def findVaccineConnect(self):
        newlist = []
        file1 = open("promptsPS16.txt", "r")
        for line in file1:
            newlist.append(line.strip().split(':'))
        for x in newlist:
            if x[0] == "indVaccineConnect":
                vacA = x[1].strip()
                vacB = x[2].strip()
                file = open("outputPS16.txt", "a")
                try:
                    list = self.bfs_sp(vacA, vacB)
                except:
                    list = []
                file.writelines("--------Function findVaccineConnect --------\n")
                file.writelines("Vaccine A " + vacA + "\n")
                file.writelines("Vaccine A " + vacB + "\n")
                if not list:
                    file.writelines("Not Related\n")
                    file.writelines("\n")
                    continue
                file.writelines("Related: Yes, ")
                for x in range(len(list) - 1):
                    file.write(list[x] + " > ")
                file.write(list[-1])
                file.writelines("\n")
                file.close()
        file1.close()




vaccineList = []  # list containing vaccine and strains
edges = []  # matrix of edges/associations
immunization = IMMUNIZATION(vaccineList, edges)
immunization.readInputfile("inputPS16.txt")
immunization.displayAll()
immunization.displayStrains()
immunization.displayVaccine()
immunization.commonStrain()
immunization.findVaccineConnect()