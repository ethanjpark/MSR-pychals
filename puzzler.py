import sys

def simlights():
	lights = [0]*int(sys.argv[1])
	#initialize light array

	for i in range(int(sys.argv[1])): #the interval iteration
		#print(i)
		for j in range(int(sys.argv[1])): #the light iteration
			#print(j)
			temp1 = i+1
			temp2 = j+1
			if((temp2)%(temp1) == 0):
				#print("j+1",temp2)
				#print("i+1",temp1)
				if(lights[j] == 1): lights[j] = 0
				else: lights[j] = 1

	print(lights[:9])


if __name__ == '__main__':
	simlights()