# ------------------------------------------------------------------------
# Please COMPLETE the IMPLEMENTATION of this class.
# Adjacent list implementation.
#
# __author__ = 'Jeffrey Chan', 'Thanawat Neamboonnum' :)
# __copyright__ = 'Copyright 2024, RMIT University'
# ------------------------------------------------------------------------
from typing import Dict, List, Set

from maze.util import Coordinates
from maze.graph import Graph


class AdjListGraph(Graph):
    """
    Represents an undirected graph.  Please complete the implementations of each method.  See the documentation for the parent class
    to see what each of the overriden methods are meant to do.
    """

    def __init__(self):
        self.adj: Dict[Coordinates, Set[Coordinates]] = {}
        self.wall: Dict[(Coordinates, Coordinates), bool] = {} # True = wall, Otherwise False
        
    def addVertex(self, label:Coordinates):
        if label not in self.adj:
            self.adj[label] = set()

    def addVertices(self, vertLabels:List[Coordinates]):
        for label in vertLabels:
            self.addVertex(label)

    def addEdge(self, vert1:Coordinates, vert2:Coordinates, addWall:bool = False)->bool:
        if vert1 in self.adj and vert2 in self.adj:
            self.adj[vert1].add(vert2)
            self.adj[vert2].add(vert1)
            self.wall[(vert1,vert2)] = addWall
            self.wall[(vert2,vert1)] = addWall
            return True
        return False

    def updateWall(self, vert1:Coordinates, vert2:Coordinates, wallStatus:bool)->bool:
        if vert1 in self.adj and vert2 in self.adj:
            self.wall[(vert1,vert2)] = wallStatus
            self.wall[(vert2,vert1)] = wallStatus
            return True
        return False

    def removeEdge(self, vert1:Coordinates, vert2:Coordinates)->bool:
        if (vert1, vert2) in self.wall:
            self.wall[(vert1,vert2)] = False
            self.wall[(vert2,vert1)] = False
            return True
        return False        


    def hasVertex(self, label:Coordinates)->bool:
        return label in self.adj


    def hasEdge(self, vert1:Coordinates, vert2:Coordinates)->bool:
        return (vert1, vert2) in self.wall

    def getWallStatus(self, vert1:Coordinates, vert2:Coordinates)->bool:
       return self.wall.get((vert1,vert2), False)

    def neighbours(self, label:Coordinates)->List[Coordinates]:
       return list(self.adj.get(label, []))
        