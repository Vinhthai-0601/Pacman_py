import random

from game import Agent
from game import Directions


class GoWestAgent(Agent):
    def getAction(self, state):
        if Directions.WEST in state.getLegalPacmanActions():
            return Directions.WEST
        else:
            return Directions.STOP


class RandomAgent(Agent):
    def getAction(self, state):
        actions = state.getLegalPacmanActions()
        random.shuffle(actions)
        return actions[0]


class SearchAgent(Agent):
    def registerInitialState(self, state):
        """
        This is the first time that the agent sees the layout of the game
        board. Here, we choose a path to the goal. In this phase, the agent
        should compute the path to the goal and store it in a local variable.
        All of the work is done in this method!

        state: a GameState object (pacman.py)
        """
        # TODO 11
        problem = self.searchType(state)  # Makes a new search problem
        self.actions = self.searchFunction(problem)  # Find a path

    def getAction(self, state):
        """
        Returns the next action in the path chosen earlier (in
        registerInitialState).  Return Directions.STOP if there is no further
        action to take.

        state: a GameState object (pacman.py)
        """
        # TODO 12
        if 'actionIndex' not in dir(self):
            self.actionIndex = 0
        i = self.actionIndex
        self.actionIndex += 1
        if i < len(self.actions):
            return self.actions[i]
        else:
            return Directions.STOP


class BFSFoodSearchAgent(SearchAgent):
    # TODO 13
    def __init__(self,SearchAgent):
        # default dictionary to store graph
        self.SearchAgent = SearchAgent

    def BFS(self):
        visited = [False] * (max(self.SearchAgent.registerInitialState()) + 1)

        # Create a queue for BFS
        queue = []
        BFSlist = []
        # Mark the source node as
        # visited and enqueue it
        queue.append(self.SearchAgent.getAction())
        visited[self.SearchAgent.getAction()] = True
        while queue:
            s = queue.pop(0)
            BFSlist.append(s)
            for i in self.SearchAgent.registerInitialState():
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
        return BFSlist
        pass


class DFSFoodSearchAgent(SearchAgent):
    # TODO 14
    pass


class UCSFoodSearchAgent(SearchAgent):
    # TODO 15
    pass


class AStarFoodSearchAgent(SearchAgent):
    # TODO 16
    pass
