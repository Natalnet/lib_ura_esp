from ControlState import ControlState

cs = ControlState() 

cs.executePrograma("FRT;FRT;ESQ;ESQ;FRT;FRT")

cs.updateExecution()
cs.showState()



cs.initTimer(10000) 

cs.updateTimer() 

