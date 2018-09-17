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
q_init = (10,10) #(x,y)
q_delta = 0.5
q_goal = (75,75)

#graph dictionary, key = coordinates, value = parent
G = {}

#list of edges (tuples)
E = []

#graph initialisation - insertion of q_init node, which is the root node.
G[q_init] = 'root'

def generate_circles(num, mean, std):
    """
    This function generates /num/ random circles with a radius mean defined by
    /mean/ and a standard deviation of /std/.

    The circles are stored in a num x 3 sized array. The first column is the
    circle radii and the second two columns are the circle x and y locations.
    """
    circles = np.zeros((num,3))
    # generate circle locations using a uniform distribution:
    circles[:,1:] = np.random.uniform(mean, dom_x-mean, size=(num,2))
    # generate radii using a normal distribution:
    circles[:,0] = np.random.normal(mean, std, size=(num,))
    return circles

# generate circles:
world = generate_circles(10, 8, 3)

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

#solve for u (source: http://paulbourke.net/geometry/pointlineplane/)
def findu(circle, node1, node2):
	numerator = (((circle[1]-node1[0])*(node2[0]-node1[0])) + ((circle[2]-node1[1])*(node2[1]-node1[1])))
	denom = euclid(node2, node1)**2
	return numerator/denom

#collision checking function
def collcheck(node1, node2):
	#collision check for each circle
	for circ in world:
		u = findu(circ, node1, node2)
		inx = node1[0]+(u*(node2[0]-node1[0]))
		iny = node1[1]+(u*(node2[1]-node1[0]))
		dist2circ = euclid((inx,iny),circ)
		#collision detected due to distance
		if(dist2circ <= circ[0]):
			return True
	return False

found = False
counter = 0
while(not found):
	if(counter > 5000): #no infinite run!
		found = True
	else:
		counter += 1
		#tuple
		q_rand = (r.randrange(dom_x), r.randrange(dom_y))
		#tuple
		q_near = fnv(q_rand)

		if(not collcheck(q_near,q_rand)):
			#add q_new to G with q_near as the parent
			G[q_rand] = q_near
			#add edge from q_new to q_near
			E.append((q_near, q_rand))

		#check if straight line path to goal exists from new node
		if(not collcheck(q_rand,q_goal)): #path to goal available
			G[q_goal] = q_rand
			E.append((q_rand, q_goal))
			found = True

verts = []
codes = []
for edge in E:
	verts.append(edge[0])
	verts.append(edge[1])
	codes.append(Path.MOVETO)
	codes.append(Path.LINETO)
fig = mp.figure()
ax = fig.add_subplot(111)
path = Path(verts, codes)
patch = patches.PathPatch(path)
ax.add_patch(patch)
fcirc = lambda x: patches.Circle((x[1],x[2]), radius=x[0], fill=True, alpha=1, fc='k', ec='k')
circs = [fcirc(x) for x in world]
for c in circs:
    ax.add_patch(c)
ax.set_xlim([0,dom_x])
ax.set_ylim([0,dom_y])
dstr = 'Number of iterations: ' + str(counter)
mp.text(25,-10,dstr)
mp.show()