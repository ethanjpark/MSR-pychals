#collatz sequence class

import copy

class collatz:

	"""constructor fills cache with sequence lengths for all integers up to
	and including 'integer'"""
	def __init__(self, integer):
		
		self.cache = {} #dictionary cache storing the sequences
		self.lencache = {}
		self.N = 0
		self.growcache(integer)

	"""fill in cache with new sequences up to new integer self.N"""
	def growcache(self, newnum):
		for i in range(self.N+1,newnum+1):
			length = 1
			term = False
			curr = copy.deepcopy(i)
			sequence = [i]
			while(not term):
				if(curr%2 == 0): #even
					curr = curr/2
					length += 1
					sequence.append(curr)
				elif((curr%2 != 0) and (curr != 1)): #odd and not 1
					curr = (3*curr) + 1
					length += 1
					sequence.append(curr)
				else: #odd and 1
					term = True
			self.cache[i] = sequence
			self.lencache[i] = length
		self.N = newnum

	"""query method for finding the sequence length for a particular integer
	or set of integers"""
	def findlens(self, inp):

		if(type(inp) == int):
			if(inp <= self.N):
				return self.lencache[inp]
			else:
				self.growcache(inp)
				return self.lencache[inp]
				#raise ValueError("Invalid integer provided.")

		elif(type(inp) == list):
			result = []
			for i in inp:
				if(i <= self.N):
					result.append(self.lencache[i])
				else:
					self.growcache(i)
					result.append(self.lencache[i])
					#raise ValueError("Invalid integer provided in list.")

			return result

	"""return the longest sequence from all sequences for up to input"""
	def retmax(self, inp):
		
		if(inp > self.N):
			self.growcache(inp)

		maxlength = 1
		champion = 0
		for i in range(1,inp+1):
			if(self.lencache[i] > maxlength):
				champion = i
				maxlength = self.lencache[i]
		return self.cache[champion]