import matplotlib.pyplot as plt
import numpy as np


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~CLASS DECLARATION~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Edge:
    def __init__(self, start, end, weight, line2D):
        self.start = start
        self.end = end
        self.weight = weight
        self.line2D = line2D

    def change_line_color(color):
        line2D.set_color(color)

class Vertex:
    def __init__(self, id, x, y, edges, dot2D, parent):
        self.id = id
        self.x = x
        self.y = y
        self.edges = edges
        self.dot2D = dot2D
        self.distance = float("inf")
        self.parent = parent

    def change_dot_color(color):
        dot2D.set_color(color)







#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~READING INPUTS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#mock inputfiles
def read_inputfile():

    #open input file for reading and place all lines in a list
    with open('input.txt', 'r') as file:
        txt = file.readlines()

    # 
    total_verts = int(txt[0].strip())
    start = int(txt[1].strip())
    end = int(txt[2].strip())

    edges_list = []
    for line in txt[3:]:
        edge = [float(component) for component in line.split()]
        
        edges_list.append(Edge(int(edge[0]), int(edge[1]), edge[2], None))

    return [edges_list, total_verts, start, end]

def read_coordinatesfile(edges: Edge):
    coords = []

    with open('coords.txt', 'r') as file:
        txt = file.readlines()
        for line in txt:
            coords.append([float(component) for component in line.split()])
            
    
    vertices = []
    for i in range(coords.__len__()):
        edge_list = []
        for edge in edges:
            if edge.start == i+1:
                edge_list.append(edge)
        vertex = Vertex(i+1, coords[i][0], coords[i][1], edge_list, None, None)
        vertices.append(vertex)
    return vertices









#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~PLOTTING GRAPH~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Create Graph
def create_graph(edges, vertices):
    fig, ax = plt.subplots(figsize=(5, 5))

    vertices = plot_vertices(ax, vertices)
    plot_edges(ax, edges, vertices)

    #plt.show()

    return vertices

#Plotting Dots
def plot_vertices(ax, vertices):
    for vertex in vertices:
        dot = ax.plot(vertex.x, vertex.y, 'o', color='black')
        vertex.dot = dot
    
    return vertices

#Plotting Edges
def plot_edges(ax, edges: Edge, coordinates):

    for edge in edges:
        x_coords = [coordinates[ edge.start -1 ].x, coordinates[ edge.end -1 ].x]
        y_coords = [coordinates[ edge.start -1].y, coordinates[ edge.end -1].y]
        line = (ax.plot(x_coords, y_coords, color="blue", linewidth=2))
        edge.line = line




#~~~~~~~~~~~~~~~~~~~~DJIKSTRA'S~~~~~~~~~~~~~~

def dijkstra_main(vertices, start, end):


    # Create unvisted set and add the start node
    unvisited = vertices[:]
    unvisited[start-1].distance = 0
    unvisited[start-1].parent = None

    # interate to every unvisited node
    while unvisited:
        current = min(unvisited, key=lambda vertex: vertex.distance) # assign the vertex with the lowest distance to current

        unvisited.remove(current) 

        # 
        for edge in current.edges:
            neighbour = vertices[edge.end-1]
            new_distance = current.distance + edge.weight

            if new_distance < neighbour.distance:
                neighbour.distance = new_distance
                neighbour.parent = current

    backtrack = vertices[end-1]

    shortest_path = []

    while backtrack.parent is not None:
        shortest_path.insert(0, backtrack.id)
        backtrack = backtrack.parent

    
    shortest_path.insert(0, backtrack.id)

    print(vertices[end-1].distance)
    print(shortest_path)
    





#~~~~~~~~~MAIN~~~~~~~~~~~~~

#readinputs
[edges, total_verts, start, end] = read_inputfile()
vertices = read_coordinatesfile(edges)

#Plot Graph
vertices = create_graph(edges, vertices)

#Run Dijkstrad
dijkstra_main(vertices, start, end)

#Complie Video















# def gpt_solution():
#     # Define the 3x3 grid of points
#     points = [(i, j) for i in range(3) for j in range(3)]

#     # Create the plot
#     fig, ax = plt.subplots()

#     # Plot the points
#     for point in points:
#         ax.plot(point[0], point[1], 'o', color='blue')

#     # Define the connections between points (as tuples of point indices)
#     connections = [
#         (0, 1), (1, 2),   # Horizontal lines in the first row
#         (3, 4), (4, 5),   # Horizontal lines in the second row
#         (6, 7), (7, 8),   # Horizontal lines in the third row
#         (0, 3), (3, 6),   # Vertical lines in the first column
#         (1, 4), (4, 7),   # Vertical lines in the second column
#         (2, 5), (5, 8)    # Vertical lines in the third column
#     ]

#     # Plot the individual lines with different colors
#     colors = ['red', 'blue', 'green', 'purple', 'orange', 'yellow', 'cyan', 'magenta', 'lime']

#     for i, (start, end) in enumerate(connections):
#         x_values = [points[start][0], points[end][0]]
#         y_values = [points[start][1], points[end][1]]
#         ax.plot(x_values, y_values, color=colors[i % 8], linewidth=2)

#     # Set limits for the axes
#     ax.set_xlim(-1, 3)
#     ax.set_ylim(-1, 3)

#     # Hide the axes
#     ax.axis('off')

#     # Show the plot
#     # plt.show()