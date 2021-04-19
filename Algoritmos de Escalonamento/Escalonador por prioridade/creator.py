# here the processes are created

from process import Process
from random import randint, randrange

def creator(processes=10):
    #creating a processes with random priorit, quantum and lifetime
    processesList = []

    for _ in range(processes):
        
        processesList.append(
            Process(
                priority=randint(0, 100), 
                quantum=randrange(1, 4),
                lifetime=randrange(1, 10)
            )
        )

    return processesList