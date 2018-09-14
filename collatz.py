#Collatz conjecture
# n --> n/2 if n is even
# n --> 3n+1 if n is odd
# everything will end at 1

import copy

champion = 0
maxlength = 0
for i in range(1000001):
	if(i%10000 == 0): print("Doing number " + str(i), end='\r')
	length = 1
	term = False
	curr = copy.deepcopy(i)
	while(not term):
		if(curr == 0): #ignore zero
			term = True
		elif(curr%2 == 0): #even
			curr = curr/2
			length += 1
		elif((curr%2 != 0) and (curr != 1)): #odd and not 1
			curr = (3*curr) + 1
			length += 1
		else: #odd and 1
			term = True

	if(length > maxlength):
		#print("Switching integer: " + str(i))
		champion = i
		maxlength = length

print("\nInteger: " + str(champion))
print("Length " + str(maxlength))