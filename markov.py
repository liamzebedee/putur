import random

class MarkovTextGenerator(object):
    def __init__(self, text):
        self.text = text
        self.words = self.processWords()
        self.cache = self.generateCache()

    # Takes self.text and yeah...
    def processWords(self):
        self.words = []
        
        #for word in self.text.split():
        #    self.words.append(word)
        for char in self.text:
        	#if char == ' ': continue
        	self.words.append(char)
        
        return self.words
    
    def triples(self):
            """ Generates triples from the given data string. So if our string were
                            "What a lovely day", we'd generate (What, a, lovely) and then
                            (a, lovely, day).
            """

            if len(self.words) < 3:
                    return

            for i in range(len(self.words) - 2):
                    yield (self.words[i], self.words[i+1], self.words[i+2])

    
    def generateCache(self):
        self.cache = {}
        for w1, w2, w3 in self.triples():
            key = (w1, w2)
            if key in self.cache:
                self.cache[key].append(w3)
            else:
                self.cache[key] = [w3]

        return self.cache
    
    def generateTextFromRandomWord(self, size=10):
        seed = random.randrange(0, len(self.words) - 3)
        seed_word, next_word = self.words[seed], self.words[seed+1]

        w1, w2 = seed_word, next_word
        gen_words = []
        spaceCnt = 0
        for i in xrange(size):
        	j = 0
        	while spaceCnt != 3:
		        if j == 23: break
		        j += 1
		        gen_words.append(w1)
		        w1, w2 = w2, random.choice(self.cache[(w1, w2)])
		        if w2 == ' ': spaceCnt += 1
		        else: spaceCnt = 0
        gen_words.append(w2)
        #print(str(gen_words))
        return ''.join(gen_words)

f = open('text.txt')
f.seek(0)
data = f.read()

markov = MarkovTextGenerator(data)
print(markov.generateTextFromRandomWord())
