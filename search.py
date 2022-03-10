"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

from game import Directions
import util
n = Directions.NORTH
s = Directions.SOUTH
e = Directions.EAST
w = Directions.WEST


def depthFirstSearch(problem):
    '''
    return a path to the goal
    '''
    # TODO 17
    startingNode = problem.getStartState()
    if problem.isGoalState(startingNode):
        return []

    myQueue = util.Stack()
    visitedNodes = []
    # (node,actions)
    myQueue.push((startingNode, []))

    while not myQueue.isEmpty():
        currentNode, actions = myQueue.pop()
        if currentNode not in visitedNodes:
            visitedNodes.append(currentNode)

            if problem.isGoalState(currentNode):
                return actions

            for nextNode, action, cost in problem.getSuccessors(currentNode):
                newAction = actions + [action]
                myQueue.push((nextNode, newAction))

    util.raiseNotDefined()

def breadthFirstSearch(problem):
    '''
    return a path to the goal
    '''
    # TODO 18

    startingNode = problem.getStartState()
    if problem.isGoalState(startingNode):
        return []

    myQueue = util.Queue()
    visitedNodes = []
    # (node,actions)
    myQueue.push((startingNode, []))

    while not myQueue.isEmpty():
        currentNode, actions = myQueue.pop()
        if currentNode not in visitedNodes:
            visitedNodes.append(currentNode)
            successors = problem.getSuccessors(currentNode)

            if problem.isGoalState(currentNode):
                return actions

            for nextNode, action, cost in successors:
                newAction = actions + [action]
                myQueue.push((nextNode, newAction))

    util.raiseNotDefined()

def uniformCostSearch(problem):
    '''
    return a path to the goal
    '''
    # TODO 19
    startingNode = problem.getStartState()
    if problem.isGoalState(startingNode):
        return []

    visitedNodes = []

    pQueue = util.PriorityQueue()
    # ((coordinate/node , action to current node , cost to current node),priority)
    pQueue.push((startingNode, [], 0), 0)

    while not pQueue.isEmpty():

        currentNode, actions, prevCost = pQueue.pop()
        if currentNode not in visitedNodes:
            visitedNodes.append(currentNode)

            if problem.isGoalState(currentNode):
                return actions

            for nextNode, action, cost in problem.getSuccessors(currentNode):
                newAction = actions + [action]
                priority = prevCost + cost
                pQueue.push((nextNode, newAction, priority), priority)

    util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def singleFoodSearchHeuristic(state, problem=None):
    """
    A heuristic function for the problem of single food search
    """
    # TODO 20
    position, foodGrid = state
    return len(foodGrid.asList())  # Gets 2/4 on autograder but expands 12517 nodes in ~9"

    # 0/4 on autograder but expands 6126 nodes in ~3"
    foodToEat = foodGrid.asList()
    totalCost = 0
    curPoint = position
    while foodToEat:
        heuristic_cost, food = \
            min([(util.manhattanDistance(curPoint, food), food) for food in foodToEat])
        foodToEat.remove(food)
        curPoint = food
        totalCost += heuristic_cost

    return totalCost
    pass


def multiFoodSearchHeuristic(state, problem=None):
    """
    A heuristic function for the problem of multi-food search
    """
    # TODO 21
    # position = state[0]
    # foodPos = []
    # for i in range(len(state) - 1):
    #     foodPos.append(state[i + 1])
    # totalH = 0
    # for food in foodPos:
    #     totalH += ((position[0] - food[0]) ** 2 + (position[1] - food[1]) ** 2) ** 0.5
    # return totalH
    print("MultipleFood")
    pass


def aStarSearch(problem, heuristic=nullHeuristic):
    '''
    return a path to the goal
    '''
    # TODO 22
    startingNode = problem.getStartState()
    if problem.isGoalState(startingNode):
        return []

    visitedNodes = []

    pQueue = util.PriorityQueue()
    # ((coordinate/node , action to current node , cost to current node),priority)
    pQueue.push((startingNode, [], 0), 0)

    while not pQueue.isEmpty():

        currentNode, actions, prevCost = pQueue.pop()

        if currentNode not in visitedNodes:
            visitedNodes.append(currentNode)

            if problem.isGoalState(currentNode):
                return actions

            for nextNode, action, cost in problem.getSuccessors(currentNode):
                newAction = actions + [action]
                newCostToNode = prevCost + cost
                heuristicCost = newCostToNode + heuristic(nextNode, problem)
                pQueue.push((nextNode, newAction, newCostToNode), heuristicCost)

    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
