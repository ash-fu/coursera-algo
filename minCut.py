# 200 vertices
from random import *
import random


def isSame(x,l):
	if len(x) == 1:
		for e in l:
			if x == [e]:
				return True
		return False
	else:
		for i in x:
			for e in l:
				if i == e:
					return True
		return False

def minCut(graph):
	if len(graph) <= 2:
		return graph
	else:
		v1_i = randint(0, len(graph)-1)
		# v1 = graph[v1_i][0]
		# print v1
		v1_edges = graph[v1_i][1]
		# print v1_edges
		v2_i = randint(0, len(v1_edges)-1)
		# print v2_i
		# v2 = v1_edges[v2_i]
		# print v2
		graph_n = contract(v1_i, v2_i, graph)
		return minCut(graph_n)

# def minCut_(graph):
# 	if len(graph) <= 2:
# 		return graph
# 	else :
# 		v1 = random.choice(graph.keys()) #get first vertices 
# 		# print v1
# 		edges = graph[str(v1)] #get all the vertices that linked to that vertice
# 		# print edges
# 		edges_n = len(edges)
# 		# print edges_n
# 		v2 = edges[randint(1,edges_n)-1]
# 		# print v2
# 		graph_n = contract(v1,v2,graph)
# 		# print graph_n
# 		return minCut(graph_n)

# def contract_(v1, v2, graph): # v1 = 2, v2 = 1, 
# 	v1 = str(v1)
# 	v2 = str(v2)
# 	print("merge " + v1 + " and " + v2 )
# 	# graph[v1] = list(set(graph[v1] + graph[v2])) #merge the edges of v1 and v2
# 	vert_n = v1+v2

# 	graph[vert_n] = graph[v1] + graph[v2]
# 	# print graph
# 	graph.pop(v1) # remove v2
# 	graph.pop(v2)
# 	# print ("remove set " + v2)
# 	print graph

# 	print("start removing self loop:")
# 	graph[vert_n] = [v for v in graph[vert_n] if not isSame(v,vert_n)] # to remove self loop
# 	print graph

# 	print("strat replacement:")

# 	for vertex, edges in graph.items(): # replace v1 with v2
# 		# for edge in edges:
# 		# 	if isSame(edge, vert_n):
# 		# edges = [vert_n for edge in edges if isSame(edge, vert_n)]

# 		for i in range(0,len(edges)): #for all the edges of vertex
# 			if isSame(edges[i],vert_n): #if the edges is same 
# 				edges[i] = vert_n
# 			# if edges[i] == : # if the chosen vert is connected
# 			# 	# print ("found v2 " + str(edges[i]) + " in key: " + str(vertice1))
# 			# 	edges[i] = v1
# 			# 	graph[vertice1] = list(set(edges))
# 				# print graph

# 	# return graph

def contract(v1_i, v2_i_, graph):
	# find v1 and v2 value
	v1 = graph[v1_i][0]
	# print v1

	v1_edges = graph[v1_i][1]
	v2 = v1_edges[v2_i_]
	# print v2

	# merge v1 and v2 as vert_n
	vert_n = v1 + v2
	# print vert_n

	# merge their edges
	# find v2 edges
	i = 0
	for i in range(0, len(graph)):
		if graph[i][0] == v2:
			v2_i = i
			v2_edges = graph[i][1]

	# merge v1 and v2 edges
	edges_n = v1_edges + v2_edges

	# remove self loop
	edges_n = [v for v in edges_n if not isSame(v,vert_n)]

	# add [ [vert_n], [edges_n] ] and delete [v1, v1_e] & [v2, v2_e]
	graph.append([vert_n, edges_n])
	graph.remove([v1, v1_edges])
	graph.remove([v2, v2_edges])
	# print graph

	# replace edges 
	j = 0
	for j in range(0, len(graph)):
		edges = graph[j][1]
		k = 0
		for k in range(0, len(edges)):
		# for e in edges:
			if isSame(edges[k], vert_n):
				edges[k] = vert_n
	# print graph
	return graph

fname = 'W4_test.txt'
# fname = 'small.txt'

with open(fname) as f:
    content = f.readlines()
alist = [x.split() for x in content] 
graph = []
for lines in alist:
	edges = []
	for e in lines[1:]:
		edges.append([e])
	graph.append([[lines[0]], edges])
# print graph
# [			[vert1,vert2], [	[vert3,vert4],	[vert5]		]		]

# contract(0,1,graph)
final = minCut(graph)
print len(final[0][1])