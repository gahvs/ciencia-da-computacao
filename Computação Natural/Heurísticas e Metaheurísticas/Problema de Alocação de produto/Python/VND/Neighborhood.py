from random import randint, shuffle
from copy import deepcopy

class Structures:
    
    @classmethod
    def _swap(cls, v, v_): return v_, v
    @classmethod
    def _randomValues(cls, i, l, v): return [randint(i, l) for _ in range(v)]

    def NS1(self, solution, n):
        positions = Structures._randomValues(0, len(solution) - 1, n)
        values = [solution[p] for p in positions]
        shuffle(values)
        neighbor = deepcopy(solution)
        for p in positions:
            neighbor[p] = values[positions.index(p)]
        return neighbor
    
    def NS2(self, solution, data, n):
        positions = Structures._randomValues(0, len(solution) - 1, n)
        neighbor = deepcopy(solution)
        for p in positions:
            neighbor[p] = randint(0, data[p]['quantity'])
        return neighbor
    
    def NS3(self, solution, data, n):
        positions = Structures._randomValues(0, len(solution) - 1, n)
        neighbor = deepcopy(solution)
        for p in positions:
            neighbor[p] = randint(0, data[p]['quantity'] // 2)
        return neighbor
    
    def NS4(self, solution, data, n):
        positions = Structures._randomValues(0, len(solution) - 1, n)
        neighbor = deepcopy(solution)
        for p in positions:
            neighbor[p] = randint(data[p]['quantity'] // 2, data[p]['quantity'])
        return neighbor