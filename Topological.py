#CS2302 Lab6-A
#By: Alejandra Maciel
#Last Modified: Dic-15-2018
#Instructor: Diego Aguirre
#TA: Manoj  Pravaka  Saha
#The purpose of this lab is to learn how to implement the Kruskal's Algorithm and the Topological Sort

#QUEUE CLASS
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)



#TOPOLOGICAL SORT METHOD
def topological(graph):
    #Get the number of vertices pointing to each vertex
    all_in_degrees = graph.compute_indegree_every_vertex()
    sort_result = []
    q = Queue()

    #Loop to find all the vertices with an indegree of 0 and enqueue them to the q list
    for i in range(len(all_in_degrees)):
        if all_in_degrees[i] == 0:
            q.enqueue(i)

    #While the q list is not empty dequeue each vertex and append it to the resultant list
    while not q.is_empty():
        u = q.dequeue()
        sort_result.append(u)

        #Loop to decrease by one the indegree of each vertex that the appended vertex point to
        for adj_vertex in graph.get_vertices_reachable_from(u):
            all_in_degrees[adj_vertex] -= 1
            #If the modified vertex's indegree becomes 0 then enqueue the vertex to the q list
            if all_in_degrees[adj_vertex] == 0:
                q.enqueue(adj_vertex)

    #If the length of the resultant list is different than the graph's number of vertices then return none
    if len(sort_result) != graph.get_num_vertices():
        return None

    #Else return the resultant list
    return sort_result
