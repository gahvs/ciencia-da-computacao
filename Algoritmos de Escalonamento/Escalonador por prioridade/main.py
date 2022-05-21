from manager import ProcessScheduler
from process import Process
from creator import creator
from time import sleep

'''
    @author: Gabriel Souto
    Implementation of the priority scheduling algorithm.
    The algorithm is preemptive and solves the starvation problem with
    the agging technique.
'''
manager = ProcessScheduler()
manager.start()

# this configuration generates a starvation problem:
manager.addProcess([Process(
    priority=1,
    quantum=5,
    lifetime=10
)])



sleep(.1)

manager.addProcess([Process(
    priority=2,
    quantum=5,
    lifetime=10
)])

# random configuration:
# processes = creator(5)
# manager.addProcess([
#     Process(
#         priority=5,
#         quantum=2,
#         lifetime=10
#     )
# ])
# manager.start()
# for process in processes:
#     manager.addProcess([process])
#     sleep(1)