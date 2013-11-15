import random

class MarkovTextGenerator(object):
	def __init__(self, text):
		self.text = text
		self.characters = [char for char in self.text]
		if len(self.characters) < 3: raise Exception("At least 3 characters needed in text")
		self.createMatrix()
	
	def characterTriples(self):
		""" Generates triples from the given data string. So if our string were
			"dogs", we'd generate (d, o, g) and then
			(o, g, s).
		"""
		for i in range(len(self.characters) - 2):
			yield (self.characters[i], self.characters[i+1], self.characters[i+2])
	
	def createMatrix(self):
		self.matrix = {}
		for char1, char2, char3 in self.characterTriples():
			key = (char1, char2)
			if key in self.matrix:
				self.matrix[key].append(char3)
			else:
				self.matrix[key] = [char3]

	def generate(self, textLength=10):
		seed = random.randrange(0, len(self.characters) - 3)
		seed_char, next_char = self.characters[seed], self.characters[seed + 1]
		
		generated_text = []
		spaceCount = 0
		char1, char2 = seed_char, next_char
		for i in range(textLength):
			j = 0
			while spaceCount != 2:
				if j == 13: break
				j += 1
				generated_text.append(char1)
				char1, char2 = char2, random.choice(self.matrix[(char1, char2)])
				if char2 == ' ': spaceCount += 1
				else: spaceCount = 0
		
		return ''.join(generated_text)

if __name__ == "__main__":
	corpus = open('text.txt').read()
	markov = MarkovTextGenerator(corpus)
	print(markov.generate())
