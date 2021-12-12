import time
class ControlState:
    kind = 'ControlState'
    def __init__(self):
        print("Control state started!")
        self.startTime = 0
        self.finalTime = 0 
        self.state = 'PAR'
        self.defaultDelta = 3000 
        self.instructionIndex = 0 
        self.instructions = [] 
        self.endExecution = False 

    def initTimer(self, dt, st):
        self.startTime = time.ticks_ms()
        self.finalTime = dt 
        self.state = st 

    def executePrograma(self, code):
        self.instructions = code.split(';')
        print(self.instructions) 
        self.initTimer(self.defaultDelta, self.instructions[0])
        self.showState() 

    def updateExecution(self): 
        print(self.endExecution)
        if self.updateTimer() and not self.endExecution : 
            self.instructionIndex += 1 
            if self.instructionIndex < len(self.instructions):
                # atualiza a instrução atual 
                self.initTimer(self.defaultDelta, self.instructions[self.instructionIndex])
            else:
                self.instructionIndex = 0 
                self.state = 'FIM' 
                self.endExecution = True  


    def updateTimer(self): 
        if ( time.ticks_diff(  time.ticks_ms(), self.startTime) < self.finalTime ):
            return False 
        else: 
            self.state = 'PAR'
            return True 
    
    def showState(self):
        print(time.ticks_ms(), self.startTime, self.finalTime, self.state) 

    
