Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:\Users\Tim\Documents\Programming\Python\Elementary-Cellular-Automata\main.py 
X X _ X _ _ X X X _ _ X X _ _ X _ X X _ X X _ _ X 
Traceback (most recent call last):
  File "C:\Users\Tim\Documents\Programming\Python\Elementary-Cellular-Automata\main.py", line 75, in <module>
    automata.run(50)
  File "C:\Users\Tim\Documents\Programming\Python\Elementary-Cellular-Automata\main.py", line 57, in run
    self.updateStrip()
  File "C:\Users\Tim\Documents\Programming\Python\Elementary-Cellular-Automata\main.py", line 48, in updateStrip
    bufferstrip[i] = int(self.dictionaryRule[self.getNeighbourhood(i)])
  File "C:\Users\Tim\Documents\Programming\Python\Elementary-Cellular-Automata\main.py", line 41, in getNeighbourhood
    right = self.strip[i + 1]
IndexError: list index out of range
>>> 
 RESTART: C:\Users\Tim\Documents\Programming\Python\Elementary-Cellular-Automata\main.py 
X X X _ X _ X X _ _ X _ X X X _ _ _ X X X X X _ X 
_ _ X X X X X X _ X X X X _ X _ _ X X _ _ _ X X X 
_ X X _ _ _ _ X X X _ _ X X X _ X X X _ _ X X _ X 
X X X _ _ _ X X _ X _ X X _ X X X _ X _ X X X X X 
_ _ X _ _ X X X X X X X X X X _ X X X X X _ _ _ _ 
_ X X _ X X _ _ _ _ _ _ _ _ X X X _ _ _ X _ _ _ _ 
X X X X X X _ _ _ _ _ _ _ X X _ X _ _ X X _ _ _ _ 
X _ _ _ _ X _ _ _ _ _ _ X X X X X _ X X X _ _ _ X 
X _ _ _ X X _ _ _ _ _ X X _ _ _ X X X _ X _ _ X X 
X _ _ X X X _ _ _ _ X X X _ _ X X _ X X X _ X X _ 
X _ X X _ X _ _ _ X X _ X _ X X X X X _ X X X X X 
X X X X X X _ _ X X X X X X X _ _ _ X X X _ _ _ _ 
X _ _ _ _ X _ X X _ _ _ _ _ X _ _ X X _ X _ _ _ X 
X _ _ _ X X X X X _ _ _ _ X X _ X X X X X _ _ X X 
X _ _ X X _ _ _ X _ _ _ X X X X X _ _ _ X _ X X _ 
X _ X X X _ _ X X _ _ X X _ _ _ X _ _ X X X X X X 
X X X _ X _ X X X _ X X X _ _ X X _ X X _ _ _ _ _ 
X _ X X X X X _ X X X _ X _ X X X X X X _ _ _ _ X 
X X X _ _ _ X X X _ X X X X X _ _ _ _ X _ _ _ X X 
_ _ X _ _ X X _ X X X _ _ _ X _ _ _ X X _ _ X X _ 
_ X X _ X X X X X _ X _ _ X X _ _ X X X _ X X X _ 
X X X X X _ _ _ X X X _ X X X _ X X _ X X X _ X _ 
X _ _ _ X _ _ X X _ X X X _ X X X X X X _ X X X X 
X _ _ X X _ X X X X X _ X X X _ _ _ _ X X X _ _ _ 
X _ X X X X X _ _ _ X X X _ X _ _ _ X X _ X _ _ X 
X X X _ _ _ X _ _ X X _ X X X _ _ X X X X X _ X X 
_ _ X _ _ X X _ X X X X X _ X _ X X _ _ _ X X X _ 
_ X X _ X X X X X _ _ _ X X X X X X _ _ X X _ X _ 
X X X X X _ _ _ X _ _ X X _ _ _ _ X _ X X X X X _ 
X _ _ _ X _ _ X X _ X X X _ _ _ X X X X _ _ _ X X 
X _ _ X X _ X X X X X _ X _ _ X X _ _ X _ _ X X _ 
X _ X X X X X _ _ _ X X X _ X X X _ X X _ X X X X 
X X X _ _ _ X _ _ X X _ X X X _ X X X X X X _ _ _ 
X _ X _ _ X X _ X X X X X _ X X X _ _ _ _ X _ _ X 
X X X _ X X X X X _ _ _ X X X _ X _ _ _ X X _ X X 
_ _ X X X _ _ _ X _ _ X X _ X X X _ _ X X X X X _ 
_ X X _ X _ _ X X _ X X X X X _ X _ X X _ _ _ X _ 
X X X X X _ X X X X X _ _ _ X X X X X X _ _ X X _ 
X _ _ _ X X X _ _ _ X _ _ X X _ _ _ _ X _ X X X X 
X _ _ X X _ X _ _ X X _ X X X _ _ _ X X X X _ _ _ 
X _ X X X X X _ X X X X X _ X _ _ X X _ _ X _ _ X 
X X X _ _ _ X X X _ _ _ X X X _ X X X _ X X _ X X 
_ _ X _ _ X X _ X _ _ X X _ X X X _ X X X X X X _ 
_ X X _ X X X X X _ X X X X X _ X X X _ _ _ _ X _ 
X X X X X _ _ _ X X X _ _ _ X X X _ X _ _ _ X X _ 
X _ _ _ X _ _ X X _ X _ _ X X _ X X X _ _ X X X X 
X _ _ X X _ X X X X X _ X X X X X _ X _ X X _ _ _ 
X _ X X X X X _ _ _ X X X _ _ _ X X X X X X _ _ X 
X X X _ _ _ X _ _ X X _ X _ _ X X _ _ _ _ X _ X X 
_ _ X _ _ X X _ X X X X X _ X X X _ _ _ X X X X _ 
_ X X _ X X X X X _ _ _ X X X _ X _ _ X X _ _ X _ 
>>> 
 RESTART: C:\Users\Tim\Documents\Programming\Python\Elementary-Cellular-Automata\main.py 
X X X X _ X X X X X X _ X X _ X X X X X _ _ _ _ X X _ X _ X 
_ _ _ X X X _ _ _ _ X X X X X X _ _ _ X _ _ _ X X X X X X X 
_ _ X X _ X _ _ _ X X _ _ _ _ X _ _ X X _ _ X X _ _ _ _ _ X 
_ X X X X X _ _ X X X _ _ _ X X _ X X X _ X X X _ _ _ _ X X 
X X _ _ _ X _ X X _ X _ _ X X X X X _ X X X _ X _ _ _ X X X 
_ X _ _ X X X X X X X _ X X _ _ _ X X X _ X X X _ _ X X _ _ 
X X _ X X _ _ _ _ _ X X X X _ _ X X _ X X X _ X _ X X X _ _ 
X X X X X _ _ _ _ X X _ _ X _ X X X X X _ X X X X X _ X _ X 
_ _ _ _ X _ _ _ X X X _ X X X X _ _ _ X X X _ _ _ X X X X X 
_ _ _ X X _ _ X X _ X X X _ _ X _ _ X X _ X _ _ X X _ _ _ X 
_ _ X X X _ X X X X X _ X _ X X _ X X X X X _ X X X _ _ X X 
_ X X _ X X X _ _ _ X X X X X X X X _ _ _ X X X _ X _ X X X 
X X X X X _ X _ _ X X _ _ _ _ _ _ X _ _ X X _ X X X X X _ X 
_ _ _ _ X X X _ X X X _ _ _ _ _ X X _ X X X X X _ _ _ X X X 
_ _ _ X X _ X X X _ X _ _ _ _ X X X X X _ _ _ X _ _ X X _ X 
_ _ X X X X X _ X X X _ _ _ X X _ _ _ X _ _ X X _ X X X X X 
_ X X _ _ _ X X X _ X _ _ X X X _ _ X X _ X X X X X _ _ _ X 
X X X _ _ X X _ X X X _ X X _ X _ X X X X X _ _ _ X _ _ X X 
_ _ X _ X X X X X _ X X X X X X X X _ _ _ X _ _ X X _ X X _ 
_ X X X X _ _ _ X X X _ _ _ _ _ _ X _ _ X X _ X X X X X X _ 
X X _ _ X _ _ X X _ X _ _ _ _ _ X X _ X X X X X _ _ _ _ X _ 
X X _ X X _ X X X X X _ _ _ _ X X X X X _ _ _ X _ _ _ X X X 
_ X X X X X X _ _ _ X _ _ _ X X _ _ _ X _ _ X X _ _ X X _ _ 
X X _ _ _ _ X _ _ X X _ _ X X X _ _ X X _ X X X _ X X X _ _ 
X X _ _ _ X X _ X X X _ X X _ X _ X X X X X _ X X X _ X _ X 
_ X _ _ X X X X X _ X X X X X X X X _ _ _ X X X _ X X X X X 
X X _ X X _ _ _ X X X _ _ _ _ _ _ X _ _ X X _ X X X _ _ _ X 
_ X X X X _ _ X X _ X _ _ _ _ _ X X _ X X X X X _ X _ _ X X 
X X _ _ X _ X X X X X _ _ _ _ X X X X X _ _ _ X X X _ X X X 
_ X _ X X X X _ _ _ X _ _ _ X X _ _ _ X _ _ X X _ X X X _ _ 
X X X X _ _ X _ _ X X _ _ X X X _ _ X X _ X X X X X _ X _ _ 
X _ _ X _ X X _ X X X _ X X _ X _ X X X X X _ _ _ X X X _ X 
X _ X X X X X X X _ X X X X X X X X _ _ _ X _ _ X X _ X X X 
X X X _ _ _ _ _ X X X _ _ _ _ _ _ X _ _ X X _ X X X X X _ _ 
X _ X _ _ _ _ X X _ X _ _ _ _ _ X X _ X X X X X _ _ _ X _ X 
X X X _ _ _ X X X X X _ _ _ _ X X X X X _ _ _ X _ _ X X X X 
_ _ X _ _ X X _ _ _ X _ _ _ X X _ _ _ X _ _ X X _ X X _ _ _ 
_ X X _ X X X _ _ X X _ _ X X X _ _ X X _ X X X X X X _ _ _ 
X X X X X _ X _ X X X _ X X _ X _ X X X X X _ _ _ _ X _ _ _ 
X _ _ _ X X X X X _ X X X X X X X X _ _ _ X _ _ _ X X _ _ X 
X _ _ X X _ _ _ X X X _ _ _ _ _ _ X _ _ X X _ _ X X X _ X X 
X _ X X X _ _ X X _ X _ _ _ _ _ X X _ X X X _ X X _ X X X _ 
X X X _ X _ X X X X X _ _ _ _ X X X X X _ X X X X X X _ X X 
_ _ X X X X X _ _ _ X _ _ _ X X _ _ _ X X X _ _ _ _ X X X _ 
_ X X _ _ _ X _ _ X X _ _ X X X _ _ X X _ X _ _ _ X X _ X _ 
X X X _ _ X X _ X X X _ X X _ X _ X X X X X _ _ X X X X X _ 
X _ X _ X X X X X _ X X X X X X X X _ _ _ X _ X X _ _ _ X X 
X X X X X _ _ _ X X X _ _ _ _ _ _ X _ _ X X X X X _ _ X X _ 
X _ _ _ X _ _ X X _ X _ _ _ _ _ X X _ X X _ _ _ X _ X X X X 
X _ _ X X _ X X X X X _ _ _ _ X X X X X X _ _ X X X X _ _ _ 
X _ X X X X X _ _ _ X _ _ _ X X _ _ _ _ X _ X X _ _ X _ _ X 
>>> 
