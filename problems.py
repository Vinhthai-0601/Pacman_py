import util
import pacman
from game import Actions
from game import Directions


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


class SingleFoodSearchProblem(SearchProblem):
    def __init__(self, startingGameState, start=None):
        # TODO 1
        self.startState = startingGameState.getPacmanPosition()
        self.walls = startingGameState.getWalls()
        if start is not None:
            self.startState = start
        print('PACMAN POSITION:', self.startState)
        print('Staring', startingGameState.getFood()[11][9])
        if (startingGameState.getNumFood() == 0):
            self.goal = self.startState
        else:
            w = 0
            while w < startingGameState.getFood().width:
                h = 0
                while h < startingGameState.getFood().height:
                    if (startingGameState.getFood()[w][h] == True):
                        self.goal = (w, h)
                        print(self.goal)
                    h += 1
                w += 1
        pass

    def getStartState(self):
        # TODO 2
        return self.startState
        pass

    def isGoalState(self, state):
        # TODO 3
        return state == self.goal
        pass

    def getSuccessors(self, state):
        # TODO 4
        successors = []
        # self._expanded += 1  # DO NOT CHANGE
        for direction in [Directions.NORTH, Directions.SOUTH, Directions.EAST, Directions.WEST]:
            x, y = state
            dx, dy = Actions.directionToVector(direction)
            nextx, nexty = int(x + dx), int(y + dy)
            if not self.walls[nextx][nexty]:
                successors.append(((nextx, nexty), direction, 1))
        return successors
        pass

    def getCostOfActions(self, actions):
        # TODO 5
        if actions is None:
            # no actions
            return -1

        x, y = self.getStartState()
        cost = 0
        for action in actions:
            # figure out the next state and see whether it's legal
            dx, dy = Actions.directionToVector(action)
            x, y = int(x + dx), int(y + dy)
            cost += 1
        return cost
        pass


class MultiFoodSearchProblem(SearchProblem):
    def __init__(self, startingGameState):
        # TODO 6
        pacmanPos, dotGrid = startingGameState.getPacmanPosition(), startingGameState.getFood()
        self.startState = (pacmanPos, dotGrid)
        self.walls = startingGameState.getWalls()
        self.startingGameState = startingGameState
        self.expanded = 0
        # Store information about heuristic
        self.heuristicInfo = {}
        pass

    def getStartState(self):
        # TODO 7
        return self.startState
        pass

    def isGoalState(self, state):
        # TODO 8
        return state[1].count() == 0
        pass

    def getSuccessors(self, state):
        # TODO 9
        successors = []
        self.expanded += 1  # DO NOT CHANGE
        for direction in [Directions.NORTH, Directions.SOUTH, Directions.EAST, Directions.WEST]:
            x, y = state[0]
            dx, dy = Actions.directionToVector(direction)
            nextx, nexty = int(x + dx), int(y + dy)
            if not self.walls[nextx][nexty]:
                nextFood = state[1].copy()
                nextFood[nextx][nexty] = False
                successors.append((((nextx, nexty), nextFood), direction, 1))
        return successors
        pass

    def getCostOfActions(self, actions):
        # TODO 10
        x, y = self.getStartState()[0]
        cost = 0
        for action in actions:
            # figure out the next state and see whether it's legal
            dx, dy = Actions.directionToVector(action)
            x, y = int(x + dx), int(y + dy)
            if self.walls[x][y]:
                return 999999
            cost += 1
        return cost
        pass
