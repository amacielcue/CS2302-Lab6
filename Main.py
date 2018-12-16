#CS2302 Lab6-A
#By: Alejandra Maciel
#Last Modified: Dic-15-2018
#Instructor: Diego Aguirre
#TA: Manoj  Pravaka  Saha
#The purpose of this lab is to learn how to implement the Kruskal's Algorithm and the Topological Sort

from Adj_List_Graph import GraphAL
from Topological import topological
from Kruskals import Graph

#Main Method
def main():

    print("\n##################################### Kruskal's Algorithm #####################################")
    print("________Original Graph________")
    #Test Graph
    graph = Graph([0, 1], 6)
    graph.add([0, 2], 1)
    graph.add([1, 2], 3)
    graph.add([1, 3], 4)
    graph.add([1, 4], 2)
    graph.add([2, 3], 7)
    graph.add([3, 4], 8)

    graph.print_graph()

    print("________After Kruskal's________")

    print("Minimum Spanning Tree: ")

    #Graph after applying Kruskal's Algorithm
    graph.kruskal()

    print("\n##################################### Topological Sort #####################################")

    #Test Graph
    graph2 = GraphAL(7, True)

    graph2.add_edge(0, 1)
    graph2.add_edge(0, 4)
    graph2.add_edge(1, 2)
    graph2.add_edge(2, 3)
    graph2.add_edge(3, 6)
    graph2.add_edge(4, 1)
    graph2.add_edge(4, 5)
    graph2.add_edge(5, 1)
    graph2.add_edge(5, 3)
    graph2.add_edge(5, 6)

    print("Unsorted Vertices:")
    for i in range(len(graph2.adj_list)):
        print(i)

    #Topological sorted vertices
    top_sort = topological(graph2)
    print("\nSorted Vertices: ")
    for j in top_sort:
        print(j)




main()