from random import choice
from time import time_ns

class Process():

    def __generateID(self):
        # id len = 7
        hx = '0123456789ABCDEF'
        id = ''
        for _ in range(7):
            id += choice(hx)

        return id


    def __init__(self, priority, quantum, lifetime, parent=None):
        self.birth = time_ns()
        self.id = self.__generateID()
        
        self.state = 2 # states: 1:running - 2: ready - 3: blocked
        self.totalCPUUsage = 0 # cpu usage  
        self.priority = priority # priority scale: 0 least priority - 100 most priority
        self.quantum = quantum # max time of execution 
        self.parent = parent # parent process
        #pointers
        self.accumulator = ''
        self.stackP = ''
        self.instructionP = ''

        self.clockWithoutExec = 0 # time in the process queue in clocks

        self.lifetime = lifetime # process lifetime for demonstration only
        
    def descProcess(self):
        # print the process's details
        print(self.__dict__)