"""
This is the file with your answer, do not rename or move it.
Write your code in it, and save it before submitting your answer.
"""
import sys
from operator import itemgetter

def find_min_path(matrix, dimensions):
    """Return both the cost of the final path and a list
    containing, in order, the value of every entry in the path.
    
    Args:
        matrix: A list with n dimensions of integers
        dimensions: A list with n elements with the dimensions of the matrix
    Returns:
        An integer with the total value of the min path,
        A list with the value of every entry on that min path
    """

    unvisited = {}
    parents = {}

    def getPermutations(list, list_of_dims):
      if len(list_of_dims) == 0:
        return list
      new_list = []
      for item in list:
        for i in range(list_of_dims[0]):
          new_list.append(item+(i,))
      return getPermutations(new_list, list_of_dims[1:])

    allNodes = getPermutations([(),], dimensions)

    for i in allNodes:
      unvisited[i] = sys.maxint
      parents[i] = None

    startNode = ()
    endNode = ()

    for i in dimensions:
      startNode = startNode + (0,)
      endNode = endNode + (i-1,)

    unvisited[startNode] = 0

    def getNeighbors(node, nodeDict):
      neighbors = []
      for i in range(len(node)):
        a = list(node)
        b = list(node)
        if node[i] + 1 < dimensions[i] and node[i] + 1 > 0:
          a[i] = node[i] + 1
          neighbors.append(tuple(a))
        if node[i] - 1 < dimensions[i] and node[i] - 1 > 0:
          a[i] = node[i] - 1
          neighbors.append(tuple(a))
      return neighbors

    def getNextNode():
      sorted_nodes = sorted(unvisited.items(), key=itemgetter(1))
      return sorted_nodes[0][0]

    def getValueAt(node, dataMatrix):
      currentMatrix = dataMatrix
      for i in node:
        currentMatrix = currentMatrix[i]
      return currentMatrix

    currentNode = None
    while currentNode != endNode:
      currentNode = getNextNode()
      currentNodeDistance = unvisited[currentNode]
      neighbors = getNeighbors(currentNode, unvisited)
      for neighbor in neighbors:
        if neighbor in unvisited:
          neighborValue = unvisited[neighbor]
          if neighborValue > currentNodeDistance + getValueAt(neighbor, matrix):
            unvisited[neighbor] = currentNodeDistance + getValueAt(neighbor, matrix)
            parents[neighbor] = currentNode
      unvisited.pop(currentNode)

    answer = [getValueAt(endNode,matrix)]
    currentNode = endNode
    while currentNode != startNode:
      currentNode = parents[currentNode]
      answer.append(getValueAt(currentNode,matrix))

    answer.reverse()
    return answer


# This tests your code with the examples given in the question, 
# and is provided only for your convenience.
if __name__ == '__main__':
    matrix1 = [[0, 10,  1, 0],
               [3, 20, 20, 0],
               [4,  4, 20, 0],
               [3,  2, 20, 0],
               [6,  7,  1, 8]]
    dimensions1 = [5, 4]
    path = find_min_path(matrix1, dimensions1)
    print path

    matrix2 = [[[1, 8, 2, 0], [0, 6, 3, 3], [0, 7, 8, 8]],
               [[5, 5, 6, 3], [1, 4, 1, 1], [0, 8, 2, 6]]]
    dimensions2 = [2, 3, 4]
    path = find_min_path(matrix2, dimensions2)
    print path

    matrix3 = [[6, 3, 5, 3, 0, 1, 1, 9],
               [5, 0, 8, 1, 9, 3, 6, 2],
               [0, 4, 5, 9, 3, 7, 4, 7],
               [2, 6, 1, 8, 8, 0, 3, 2],
               [0, 6, 6, 5, 4, 7, 9, 1],
               [4, 8, 1, 7, 2, 9, 5, 3]]
    dimensions3 = [6, 8]
    path = find_min_path(matrix3, dimensions3)
    print path