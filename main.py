# Written by Long Yang Paffrath
true = True
false = False
# mem = [[(1, 100), (3, 50)], [(2, 50), (4, 80), (3, 100)], [(1, 50), (4, 50)], [
#    (0, 50), (1, 100), (4, 250)], [(3, 250), (1, 80), (2, 50)]]
mem = [[(1, 5), (3, 5), (4, 8)], [(0, 5), (2, 5), (3, 2), (5, 4)], [(1, 5), (5, 6)], [
    (0, 5), (1, 2)], [(0, 8), (7, 4)], [(1, 4), (2, 6), (6, 4), (7, 1)], [(5, 4)], [(4, 4), (5, 1)]]
nodeCounter = 8
start = None
dijkstraTable = []


def getCost(node):
    cost = 0
    nextNode = node
    while nextNode != '-':
        cost += dijkstraTable[nextNode][0]
        nextNode = dijkstraTable[nextNode][1]
    return cost


def initDijkstra():
    del dijkstraTable[:]
    for _ in range(nodeCounter):
        dijkstraTable.append((float('inf'), '-'))
        dijkstraTable[start] = (0, '-')


def calcTable():
    initDijkstra()
    currentNode = start
    visited = [start]
    while (len(visited) < nodeCounter):
        print('Beginn tests for Node %i' % (currentNode))
        for bracket in mem[currentNode]:
            #print('Testing for connection to %i' % (bracket[0]))
            if (getCost(currentNode) + bracket[1] < dijkstraTable[bracket[0]][0]):
                dijkstraTable[bracket[0]] = (
                    getCost(currentNode) + bracket[1], currentNode)
        print(dijkstraTable)
        smallestEntry = None
        for i in range(len(dijkstraTable)):
            if (i not in visited and smallestEntry == None):
                smallestEntry = i
            elif (smallestEntry != None and dijkstraTable[smallestEntry][0] > dijkstraTable[i][0] and i not in visited):
                smallestEntry = i
        visited.append(smallestEntry)
        currentNode = smallestEntry


def findRoute(node):
    route = []
    nextNode = node
    while nextNode != '-':
        route.append(nextNode)
        nextNode = dijkstraTable[nextNode][1]
    return route[:: -1]


if __name__ == "__main__":
    print('Written by Long Yang Paffrath')
    print('')
    print('addNode to add a new node')
    print('connect [nodeA] [nodeB] [cost] to connect two nodes')
    print('startNode [node] to specify the startnode')
    print(
        'route [node] to find the fastest route from the startnode to the specified node')
    print('nodes to print all stored nodes')
    print('output [m/l] to output in the given format')
    print('clear to clear current memory')
    print('exit to exit')

    print('There is an example saved in the memory!')
    while true:
        x = str(input('>'))
        cmd = x.split(' ')
        if (cmd[0] == 'addNode'):
            mem.append([])
            print('Added Node "%i"' % (nodeCounter))
            nodeCounter += 1
        elif (cmd[0] == 'startNode'):
            start = int(cmd[1])
            print('Startnode set to: %i' % (int(cmd[1])))
        elif (cmd[0] == 'route'):
            print('Calculating Dijkstra table...')
            calcTable()
            print("Route:")
            print(findRoute(int(cmd[1])))
            print("Cost:")
            print(dijkstraTable[int(cmd[1])][0])
        elif (cmd[0] == 'nodes'):
            print('Nodes:')
            for i in range(nodeCounter):
                print('ID: %i is in memory' % (i))
        elif (cmd[0] == 'connect'):
            try:
                mem[int(cmd[2])]
            except IndexError:
                print('Node "%i" does not exist' % (int(cmd[2])))
            mem[int(cmd[1])].append((int(cmd[2]), int(cmd[3])))
            mem[int(cmd[2])].append((int(cmd[1]), int(cmd[3])))

        elif (cmd[0] == 'output'):
            if (cmd[1] == 'm'):
                matr = []
                # Initiate matrix thingy
                for i in range(nodeCounter):
                    matr.append([])
                    for j in range(nodeCounter):
                        matr[i].append(float('inf'))
                for i in range(nodeCounter):
                    for j in mem[i]:
                        matr[i][j[0]] = j[1]
                print('Matrix output:')
                print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                                 for row in matr]))
            elif (cmd[1] == 'l'):
                for i in range(nodeCounter):
                    put = str(i) + " -> "
                    for j in mem[i]:
                        put += '[' + str(j[0]) + '/' + str(j[1]) + '] -> '
                    put += '[/]'
                    print(put)
            else:
                print('Invalid argument: %s' % (cmd[1]))
        elif (cmd[0] == 'clear'):
            mem = []
            nodeCounter = 0
            print('Memory cleared')
        elif (cmd[0] == 'exit'):
            break
        else:
            print('Unknown command')
