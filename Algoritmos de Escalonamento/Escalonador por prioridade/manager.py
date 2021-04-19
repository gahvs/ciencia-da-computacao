from threading import Thread
from time import sleep, time_ns

class ProcessScheduler(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.processesList = []
        self.clockWithoutExecutionLimit = 2

    def __listProcessesIsEmpty(self):
        return len(self.processesList) == 0

    def __sortByPriority(self):
        self.processesList.sort(key=lambda process: process.priority, reverse=True)

    def __increasesPriority(self, process):
        # increments the priority of a process
        process.priority += 1

    def __increasesClockWithoutExec(self):
        # increments the attribute clockWithoutExec for each process,
        # except the process that is running or blocked
        for process in self.processesList:
            if process.state == 2:
                process.clockWithoutExec += 1
                if process.clockWithoutExec == self.clockWithoutExecutionLimit:
                    self.__increasesPriority(process)
                    process.clockWithoutExec = 0

    def __changeStateOfRunningProcess(self):
        for process in self.processesList:
            if process.state == 1:
                process.state = 2
                break

    def __selectProcess(self, cpuUsageTime):
        # manager's core
        # selects and returns the process's index in accord with priority and cpu usage
        # returns a process's index or None
        for process in self.processesList:
            if process.state == 2 and process.quantum > cpuUsageTime:
                return self.processesList.index(process)
        
        return None

    def addProcess(self, processes):
        for process in processes:
            self.processesList.append(process)

    def run(self):
        start = time_ns()
        # clock = 100ms
        cpuUsageTime = 0

        while True:
            self.__sortByPriority()
            self.__changeStateOfRunningProcess()
            # take the highest priority process with state = ready 
            # and processing time < quantum
            # self.processesList[i] is more priority and is ready
            i = None      
            while i is None:
                i = self.__selectProcess(cpuUsageTime)

            print('running process: ', self.processesList[i].id)
            self.processesList[i].state = 1
            self.__increasesClockWithoutExec()
            self.processesList[i].totalCPUUsage += 1
            cpuUsageTime += 1

            if self.processesList[i].lifetime == self.processesList[i].totalCPUUsage:
                # finished
                print('process', self.processesList[i].id, 'finished')
                
                self.processesList.remove(self.processesList[i])
                cpuUsageTime = 0
            
            if self.__listProcessesIsEmpty():
                end = time_ns()
                print('\nempty process list... runtime: %fsec' % ((end-start) / 10 ** 9))
                break

            if self.processesList[i].quantum == cpuUsageTime:
                cpuUsageTime = 0

            sleep(.5) # sleeps for 100ms - 1 clock