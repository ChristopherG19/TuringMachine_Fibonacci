import itertools

class Tape():
    def __init__(self, input, blank):
        
        self.cells = [blank for i in range(50000)]
        self.actualPos = 0
        self.output = ''
        self.cells = [x for x, y in itertools.zip_longest(input, self.cells, fillvalue='B')]

    def isEnd(self):
        return self.actualPos < 0 or self.actualPos >= len(self.cells)

    def read(self):
        if self.isEnd():
            return -1
        else:
            return self.cells[self.actualPos]
        
    def lectorPosition(self):
        return self.actualPos
    
    def resetPosLector(self):
        self.actualPos = 0
        
    def write(self, symbol):
        self.cells[self.actualPos] = symbol
        
    def move(self, direction):
        if self.isEnd():
            raise Exception('Fin de la máquina')
        if (direction == 'R'):
            self.actualPos += 1
        elif (direction == 'L'):
            self.actualPos -= 1
   
    def getResult(self):
        return self.output
    
    def extractOutput(self):
        values = []
        actPos = 0
        while(actPos < len(self.cells)):
            if(self.cells[actPos] != 'B'):
                values.append(self.cells[actPos])
            actPos += 1
        self.output = "".join(values)
    
    def __str__(self):
        return str(self.cells)
        
class TM():
    def __init__(self, input, transitions, inState, fnState, blank):
        self.transitions = transitions
        self.finalState = fnState
        self.actualState = inState
        self.blank = blank
        self.tape = Tape(input, self.blank)
        
    def read(self):
        symbol = self.tape.read()
        return symbol if((self.actualState, symbol) not in self.transitions) else None
    
    def fibonacci(self):
        while (self.actualState != self.finalState):
            symbol = self.tape.read()
            if symbol is None: return None 
            try:
                destiny, newSymbol, direction = self.transitions[(self.actualState, symbol)]
                self.actualState = destiny
                self.tape.write(newSymbol)
                self.tape.move(direction)
                
                if (self.actualState == self.finalState):
                    self.tape.output += symbol
            except:
                print((self.actualState, symbol))
                
        self.tape.extractOutput()
        return self.tape.getResult()
            
