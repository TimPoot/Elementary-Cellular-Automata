import random

class ElementaryCellularAutomata:

    #initialize instance, takes lengt of strip as int and a Wolfram Rule as int
    #length is length of the strip
    #both Rule variables are representations of the Wolfram rule, decimal in decimal int format
    #and dictionary as a 3 bitstring -> T/F mapping
    #strip is a list of integers, range(0, 1)
    def __init__(self, length, rule):
        self.length = length
        self.decimalRule = rule
        self.dictionaryRule = dict()

        self.strip = self.getRandomStrip()
        self.initRule()

    def getRandomStrip(self):
        randomStrip = list()
        for i in range(0, self.length):
            randomStrip.append(random.randint(0, 1)) 
        return randomStrip

    #initializes a rule dictionary from the decimal rule
    #format {'101' = '0', ... , '11'='1'}
    def initRule(self):
        binaryRule = self.toBinaryString(self.decimalRule)
        dictionaryKey =  7

        #prepend 0s for full dictionary
        while len(binaryRule) < 8:
            binaryRule = "0" + binaryRule
        #build dictionary by tierating over bitstring and assigning each character to corresponding 3bit key
        for c in binaryRule:
            self.dictionaryRule[self.toBinaryString(dictionaryKey)] = c
            dictionaryKey -= 1

    def getNeighbourhood(self, i):
        left = self.strip[i - 1]
        center = self.strip[i]
        right = self.strip[(i + 1) % self.length]
        neighbourhood = 100 * left + 10 * center + right
        return str(neighbourhood)

    def updateStrip(self):
        bufferstrip = list(self.strip)
        for i in range(0, self.length):
            bufferstrip[i] = int(self.dictionaryRule[self.getNeighbourhood(i)])
        self.strip = bufferstrip          

    def toBinaryString(self, x):
        return str(bin(x).replace("0b", ""))

    #updates the automata n times
    def run(self, n):
        self.printStrip()
        for i in range(0, n):
            self.updateStrip()
            self.printStrip()
    
    def printStrip(self):
        for i in range(0, self.length):
            if self.strip[i]:
                print('X', end='', flush=True)
            else:
                print('_', end='', flush=True)
        print()

    #used for debugging
    def testPrint(self):
        print("Strip: " + str(self.strip))
        print("Decimal rule: " + str(self.decimalRule))
        print("dictionaryRule: " + str(self.dictionaryRule))

automata = ElementaryCellularAutomata(25, 110)
automata.run(50)
