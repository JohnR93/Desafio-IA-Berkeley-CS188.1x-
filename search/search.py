# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
"""

import util
import copy

from game import Directions
n = Directions.NORTH
s = Directions.SOUTH
e = Directions.EAST
w = Directions.WEST

class SearchProblem:
  """
  This class outlines the structure of a search problem, but doesn't implement
  any of the methods (in object-oriented terminology: an abstract class).
  
  You do not need to change anything in this class, ever.
  """
  
  def getStartState(self):
     """
     Returns the start state for the search problem 
     """
     util.raiseNotDefined()
    
  def isGoalState(self, state):
     """
       state: Search state
    
     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state
     
     For a given state, this should return a list of triples, 
     (successor, action, stepCost), where 'successor' is a 
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental 
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take
 
     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()
           

def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
  """
  Search the deepest nodes in the search tree first [p 85].
  
  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm [Fig. 3.7].
  
  To get started, you might want to try some of these simple commands to
  understand the search problem that is being passed in:
  
  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  """
  "*** YOUR CODE HERE ***"

  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  
  startState = (problem.getStartState(), [])
  pilha = util.Stack()
  pilha.push(startState)
  percorrido = []

  while not pilha.isEmpty():
    extraido = pilha.pop()
    posicaoAtual = extraido[0]
    caminho = extraido[1]

    if posicaoAtual not in percorrido:
      percorrido.append(posicaoAtual)
      if problem.isGoalState(posicaoAtual):
        return caminho
      proximoEstado = problem.getSuccessors(posicaoAtual)

      for i in list(proximoEstado):
        if proximoEstado[0] not in percorrido:
          pilha.push((i[0], caminho + [i[1]]))

def breadthFirstSearch(problem):
  """
  Search the shallowest nodes in the search tree first.
  [2nd Edition: p 73, 3rd Edition: p 82]
  """
  "*** YOUR CODE HERE ***"
  startState = (problem.getStartState(), [])
  fila = util.Queue()
  fila.push(startState)
  percorrido = []

  while not fila.isEmpty():
    extraido = fila.pop()
    posicaoAtual = extraido[0]
    caminho = extraido[1]

    if posicaoAtual not in percorrido:
      percorrido.append(posicaoAtual)
      if problem.isGoalState(posicaoAtual):
        return caminho
      proximoEstado = problem.getSuccessors(posicaoAtual)

      for i in list(proximoEstado):
        if proximoEstado[0] not in percorrido:
          fila.push((i[0], caminho + [i[1]]))
  
  
  util.raiseNotDefined()
      
def uniformCostSearch(problem):
  "Search the node of least total cost first. "
  "*** YOUR CODE HERE ***"
  startState = (problem.getStartState())
  filaPrioritaria = util.PriorityQueue()
  percorrido = {}
  custo = 0
  acoes = []
  filaPrioritaria.push((startState, acoes, custo), custo)

  while not filaPrioritaria.isEmpty():
    extraido = filaPrioritaria.pop()

    if problem.isGoalState(extraido[0]):
      return extraido[1]
    if extraido[0] not in percorrido:
      percorrido[extraido[0]] = True
      for i1, i2, i3 in problem.getSuccessors(extraido[0]):
        if i1 and i1 not in percorrido:
          filaPrioritaria.push((i1, extraido[1] + [i2], extraido[2] + i3), extraido[2] + i3)

  util.raiseNotDefined()

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  "*** YOUR CODE HERE ***"
  startState = (problem.getStartState())
  filaPrioritaria = util.PriorityQueue()
  percorrido = {}
  custo = 0
  acoes = []
  filaPrioritaria.push((startState, acoes, custo), custo)

  while not filaPrioritaria.isEmpty():
    extraido = filaPrioritaria.pop()

    if problem.isGoalState(extraido[0]):
      return extraido[1]
    if extraido[0] not in percorrido:
      percorrido[extraido[0]] = True
      for i1, i2, i3 in problem.getSuccessors(extraido[0]):
        if i1 and i1 not in percorrido:
          filaPrioritaria.push((i1, extraido[1] + [i2], extraido[2] + i3), extraido[2] + i3 + heuristic(i1, problem))

  util.raiseNotDefined()
    
  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch