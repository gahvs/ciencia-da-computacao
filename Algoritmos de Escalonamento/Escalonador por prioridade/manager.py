from threading import Thread
from time import sleep, time_ns
from process import Process
class ProcessScheduler(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.__processesList = []
        self.__completedProcess = []
        self.__clockWithoutExecutionLimit = 2
        self.__waitingTime = 0
        self.__processingTime = 0

    def addProcess(self, processes):
        for process in processes:
            self.__processesList.append(process)
            process.setQueueEntry(time=time_ns())

    def __listProcessesIsEmpty(self):
        return len(self.__processesList) == 0

    def __sortByPriority(self):
        self.__processesList.sort(key=lambda process: process.getPriority(), reverse=True)

    def __increasesClockWithoutExecOfProcess(self):
        # increments the attribute clockWithoutExec for each process,
        # except the process that is running or blocked
        for process in self.__processesList:
            if process.isReady():
                process.incrementClocksWithoutExec()
                if process.getClocksWithouExec() == self.__clockWithoutExecutionLimit:
                    process.incrementPriotity()
                    process.resetClocksWithoutExec()

    def __changeStateOfRunningProcess(self):
        process = Process.getRunnningProcess(self.__processesList)
        if process is not None:
            process.setReadyState()
            process.incrementTotalProcessingTime(finishedProcessingTime=time_ns())
            process.resetStartProcessing()

    def __selectProcess(self, cpuUsageTime):
        # manager's core
        # selects and returns the process's index in accord with priority and cpu usage
        # returns a process's index or None
        for process in self.__processesList:
            if process.isReady() and process.getQuantum() > cpuUsageTime:
                return self.__processesList.index(process)
        
        return None

    def __detail(self):
        np = len(self.__completedProcess)
        avgWT = self.__waitingTime / np
        avgPT = self.__processingTime / np
        print('average waiting time: %fsec(s)' % (avgWT / (10 ** 9)))
        print('average processing time: %fsec(s)' % (avgPT / (10 ** 9)))

    def run(self):
        start = time_ns()
        # clock = 100ms
        cpuUsageTime = 0

        while True:
            self.__sortByPriority()
            self.__changeStateOfRunningProcess()
            # take the highest priority process with state = ready 
            # and processing time < quantum
            # self.__processesList[i] is more priority and is ready
            i = None      
            while i is None:
                i = self.__selectProcess(cpuUsageTime)

            print('running process: ', self.__processesList[i].getID())
            self.__processesList[i].setRunningState()
            self.__processesList[i].setStartProcessing(time=time_ns())
            self.__increasesClockWithoutExecOfProcess()
            self.__processesList[i].incrementCPUUsage()
            cpuUsageTime += 1

            if self.__processesList[i].getLifetime() == self.__processesList[i].getTotalCPUUsage():
                # finished
                print('process', self.__processesList[i].getID(), 'finished')
                self.__completedProcess.append(self.__processesList[i])
                self.__processesList[i].setQueueExit(time=time_ns())
                self.__waitingTime += self.__processesList[i].getTotalWaitingTime()
                self.__processingTime += self.__processesList[i].getTotalProcessingTime()
                self.__processesList.remove(self.__processesList[i])
                cpuUsageTime = 0
            
            if self.__listProcessesIsEmpty():
                end = time_ns()
                print('\nempty process list... runtime: %fsec(s)' % ((end-start) / 10 ** 9))
                self.__detail()
                break

            if self.__processesList[i].getQuantum() == cpuUsageTime:
                cpuUsageTime = 0

            sleep(.5) # sleeps for 500ms - 1 clock