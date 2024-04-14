# ------------------------------------------------------------------------
# Please COMPLETE the IMPLEMENTATION of this class.
# Adjacent matrix implementation.
#
# __author__ = 'Jeffrey Chan', 'Thanawat Neamboonnum' :)
# __copyright__ = 'Copyright 2024, RMIT University'
# ------------------------------------------------------------------------
from typing import List

from maze.util import Coordinates
from maze.graph import Graph


class AdjMatGraph(Graph):
    def __init__(self):
        self.vertices = []
        self.metrix = []

    def addVertex(self, label:Coordinates):
        # Add a new vertex if it's not already in the list
        if label not in self.vertices:
            self.vertices.append(label)
            # Add a new row and column in the metrix for the new vertex
            for row in self.metrix:
                row.append(0) # init new edge as 0 (no wall/edge)
            self.metrix.append([0] * (len(self.vertices))) # New row for the new vertex

    def addVertices(self, vertLabels:List[Coordinates]):
        for label in vertLabels: 
            self.addVertex(label)

    def addEdge(self, vert1:Coordinates, vert2:Coordinates, addWall:bool = False)->bool:
        # Add an edge between vert1 and vert2
        if vert1 in self.vertices and vert2 in self.vertices:
            idx1 = self.vertices.index(vert1)
            idx2 = self.vertices.index(vert2)
            self.metrix[idx1][idx2] = 1 if addWall else 0
            self.metrix[idx2][idx1] = 1 if addWall else 0
            return True
        return False

    def updateWall(self, vert1:Coordinates, vert2:Coordinates, wallStatus:bool)->bool:
        # update wall status of wall between vert1 and vert2
        if vert1 in self.vertices and vert2 in self.vertices:
            idx1 = self.vertices.index(vert1)
            idx2 = self.vertices.index(vert2)
            self.metrix[idx1][idx2] = 1 if wallStatus else 0
            self.metrix[idx2][idx1] = 1 if wallStatus else 0
            return True
        return False

    def removeEdge(self, vert1:Coordinates, vert2:Coordinates)->bool:
        # remove edge between vert1 and vert2 
        return self.updateWall(vert1,vert2, False)

    def hasVertex(self, label:Coordinates)->bool:
        return label in self.vertices

    def hasEdge(self, vert1:Coordinates, vert2:Coordinates)->bool:
        if vert1 in self.vertices and vert2 in self.vertices:
            idx1 = self.vertices.index(vert1)
            idx2 = self.vertices.index(vert2)
            return self.metrix[idx1][idx2] == 1
        return False

    def getWallStatus(self, vert1:Coordinates, vert2:Coordinates)->bool:
        if vert1 in self.vertices and vert2 in self.vertices:
            idx1 = self.vertices.index(vert1)
            idx2 = self.vertices.index(vert2)
            return self.metrix[idx1][idx2] == 1
        return False

    def neighbours(self, label:Coordinates)->List[Coordinates]:
        if label in self.vertices:
            idx = self.vertices.index(label)
            return [self.vertices[i] for i in range(len(self.metrix)) if self.metrix[idx][i] == 1]
        return []
        