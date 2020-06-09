import sys
import random

def getBestTask(candidates, tasks):
    '''
    Finds the best task to be selected
    :param candidates: set of available candidate tasks
    :param tasks: time required for each task
    :return: the task with minimum time
    '''
    bestTimeTask = sys.maxsize
    bestTask = 0
    for c in candidates:
        time = tasks[c]
        if time < bestTimeTask:
            bestTimeTask = time
            bestTask = c
    return bestTask


def greedyWaitingTime(tasks):
    # Initially, all tasks are candidates
    candidates = set()
    n = len(tasks)
    for i in range(n):
        candidates.add(i)
    sol = []
    while candidates:
        # In each step, we select the best task
        # This is ineffficient, no need to traverse the complete task list
        # in each iteration
        bestTask = getBestTask(candidates, tasks)
        candidates.remove(bestTask)
        sol.append(bestTask)
    return sol


n = 10
tasks = []
for i in range(n):
    tasks.append(random.uniform(44, 140))
print(tasks)
sol = greedyWaitingTime(tasks)
sumWaitingTime = 0
for t in sol:
    print(str(t), end=" ")
    sumWaitingTime += tasks[t]
print()
print("SUM: "+str(sumWaitingTime))
print("AVG: "+str(sumWaitingTime/n))
