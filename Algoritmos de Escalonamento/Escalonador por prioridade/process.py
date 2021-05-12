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
        self.__birth = time_ns()
        self.__id = self.__generateID()
        
        self.__state = 2 # states: 1:running - 2: ready - 3: blocked
        self.__totalCPUUsage = 0 # cpu usage  
        self.__priority = priority # priority scale: 0 least priority - 100 most priority
        self.__quantum = quantum # max time of execution 
        self.__parent = parent # parent process
        #pointers
        self.__accumulator = ''
        self.__stackP = ''
        self.__instructionP = ''

        self.__clockWithoutExec = 0 # time in the process queue in clocks

        self.__lifetime = lifetime # process lifetime for demonstration only
        self.__totalProcessingTime = 0
        self.__startProcessing = 0
        self.__queueEntry = 0
        self.__queueExit = 0

    def descProcess(self):
        # print the process's details
        print(self.__dict__)

    def getBirth(self):
        return self.__birth
    def getID(self):
        return self.__id
    def getTotalCPUUsage(self):
        return self.__totalCPUUsage
    def getQuantum(self):
        return self.__quantum
    def getPriority(self):
        return self.__priority
    def getLifetime(self):
        return self.__lifetime
    def getState(self):
        return self.__state
    def getClocksWithouExec(self):
        return self.__clockWithoutExec
    def getTotalQueueTime(self):
        return (self.__queueExit - self.__queueEntry)
    def getTotalProcessingTime(self):
        return self.__totalProcessingTime
    def getTotalWaitingTime(self):
        return (self.getTotalQueueTime() - self.getTotalProcessingTime())

    def setRunningState(self):
        self.__state = 1
    def setReadyState(self):
        self.__state = 2
    def setBlockedState(self):
        self.__state = 3
    def setQueueEntry(self, time):
        self.__queueEntry = time
    def setQueueExit(self, time):
        self.__queueExit = time
    def setStartProcessing(self, time):
        self.__startProcessing = time
    def incrementCPUUsage(self):
        self.__totalCPUUsage += 1
    def incrementPriotity(self):
        self.__priority += 1
    def resetClocksWithoutExec(self):
        self.__clockWithoutExec = 0
    def resetStartProcessing(self):
        self.__startProcessing = 0
    def incrementClocksWithoutExec(self):
        self.__clockWithoutExec += 1
    def incrementTotalProcessingTime(self, finishedProcessingTime):
        self.__totalProcessingTime += (finishedProcessingTime - self.__startProcessing)

    def isRunning(self):
        return self.__state == 1
    def isReady(self):
        return self.__state == 2
    def isBlocked(self):
        return self.__state == 3
    
    @staticmethod
    def getRunnningProcess(processes):
        p = list(filter(lambda process: process.isRunning(), processes))
        return p[0] if len(p) else None