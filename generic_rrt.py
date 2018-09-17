"""
G.init(q_init)
for k = 1 to K:
	RAND_CONF() = q_rand
	NEAREST_VERTEX(q_rand, G) = q_near
	NEW_CONFIG(q_near,q_rand,q_delta) = q_new
	G.add_vertex(q_new)
	G.add_edge(q_near,q_new)
return G
"""

import numpy as np
from scipy.misc import imread
import matplotlib.pyplot as mp
from matplotlib.path import Path
import matplotlib.patches as patches
import random as r
import math

#given params
dom_y = 100
dom_x = 100
q_init = (50,50) #(x,y)
q_delta = 1

#number of iterations
K = 500

#graph dictionary, key = coordinates, value = parent
G = {}

#list of edges (tuples)
E = []

#graph initialisation - insertion of q_init node, which is the root node.
G[q_init] = 'root'

#find the euclidean distance between two nodes
def euclid(node1, node2):
	x = node1[0]-node2[0]
	y = node1[1]-node2[1]
	return math.sqrt((x**2)+(y**2))

#find the nearest vertex given target node
def fnv(target):
	mindist = math.sqrt((dom_y**2)+(dom_x**2))
	nv = (dom_y+1,dom_x+1)
	for coord in G.keys():
		dist = euclid(target, coord)
		if(dist < mindist):
			mindist = dist
			nv = coord
	return nv

#find the new node given q_near and q_rand
def findnew(near, rand):
	x = (rand[0]-near[0])*q_delta
	y = (rand[1]-near[1])*q_delta
	return (near[0]+x, near[1]+y)

for i in range(K):
	#tuple
	q_rand = (r.randrange(dom_x), r.randrange(dom_y))
	#tuple
	q_near = fnv(q_rand)
	#tuple
	q_new = findnew(q_near, q_rand)
	#add q_new to G with q_near as the parent
	G[q_new] = q_near
	#add edge from q_new to q_near
	E.append((q_new, q_near))

verts = []
codes = []
for edge in E:
	verts.append(edge[0])
	verts.append(edge[1])
	codes.append(Path.MOVETO)
	codes.append(Path.LINETO)
fig = mp.figure()
path = Path(verts, codes)
patch = patches.PathPatch(path)
ax = fig.add_subplot(111)
ax.add_patch(patch)
ax.set_xlim([0,dom_x])
ax.set_ylim([0,dom_y])
dstr = 'Number of iterations: ' + str(K)
mp.text(25,-10,dstr)
mp.show()