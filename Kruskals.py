#CS2302 Lab6-A
#By: Alejandra Maciel
#Last Modified: Dic-15-2018
#Instructor: Diego Aguirre
#TA: Manoj  Pravaka  Saha
#The purpose of this lab is to learn how to implement the Kruskal's Algorithm and the Topological Sort

class Graph:

    E = []
    W = []
    V = []

    def __init__(self, edge_list, weight):
        self.E.append(edge_list)
        self.W.append(weight)

    #Sort sets by weight
    def sort(self):
        if len(self.E) != len(self.W):
            return

        for i in range(1, len(self.W)):
            temp_weight = self.W[i]
            temp_edge = self.E[i]
            temp = i - 1

            while temp >= 0 and temp_weight < self.W[temp]:
                self.W[temp + 1] = self.W[temp]
                self.E[temp + 1] = self.E[temp]
                temp -= 1

            self.W[temp + 1] = temp_weight
            self.E[temp + 1] = temp_edge

    #Create new sets
    def build(self):
        for i in range(len(self.E)):
            for j in range(len(self.E[i])):
                if self.E[i][j] not in self.V:
                    self.V.append(self.E[i][j])

        for k in range(len(self.V)):
            self.V[k] = [self.V[k]]

    #Find sets
    def find(self, vertex):
        for i in range(len(self.V)):
            for element in self.V[i]:
                if element == vertex:
                    return i
        return None

    #Combine sets
    def union(self, vertex1, vertex2):
        index1 = self.find(vertex1)
        index2 = self.find(vertex2)
        for element in self.V[index2]:
            self.V[index1].append(element)
        self.V.pop(index2)

    #Add edge with respective weight
    def add(self, edge_list, weight):
        self.E.append(edge_list)
        self.W.append(weight)

    #Kruskal's Algorithm
    def kruskal(self):
        self.sort()
        self.build()
        count, i = 0, 0

        while len(self.V) > 1:

            if self.find(self.E[i][0]) != self.find(self.E[i][1]):
                print("[%d, %d]" % (self.E[i][0], self.E[i][1]))
                count += 1
                self.union(self.E[i][0], self.E[i][1])
            i += 1

    #Print Graph Method
    def print_graph(self):
        print("Edges:")
        print(self.E)
        print("Weights:")
        print(self.W)