import random


nodes = 1000
connectionProbability = 1/nodes


class Probe:
    def __init__(self, location, visited):
        self.location = location
        self.visited = visited
    
    def __repr__(self):
        return str(self.location)


def generateStructure(nodes):
    structure: list[list] = [[] for _ in range(nodes)]
    for i in range(nodes):
        for a in range(nodes):
            if i == a:
                continue
            if random.random() <= connectionProbability and a not in structure[i]:
                structure[i].append(a)
                structure[a].append(i)
    return structure


structure = generateStructure(nodes)
probes = [Probe(0, [])]
newProbes = []
successfulProbes = []
visitedNodes = []
goal = nodes-1
finished = False

while True:
    newProbes = []
    for probe in probes:
        if probe.location == goal:
            finished = True
            successfulProbes.append(Probe(probe.location, probe.visited+[goal]))
            continue
        for connection in structure[probe.location]:
            if connection not in visitedNodes:
                visitedNodes.append(connection)
                newProbes.append(Probe(connection, probe.visited+[probe.location]))
    probes = newProbes.copy()
    if not newProbes or finished:
        break

if successfulProbes:
    print([p.visited for p in successfulProbes])
else:
    print("No connection to goal possible.")
