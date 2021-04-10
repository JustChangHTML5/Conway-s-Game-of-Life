from ast import literal_eval

"""
Functions:
  Matrix.build:
    Builds the Matrix

  Matrix.get:
    Returns a Node Based on its Xm and Ym

  Matrix.find:
    Returns all Nodes that have a Certain Key

  Matrix.save:
    Saves the Matrix in a text Document

  Matrix.load:
    Loads a Saved text Document
"""


class MatrixNode:
    def __init__(self, key, Xm, Ym):
        self.key = key
        self.Xm = Xm
        self.Ym = Ym

    def transmit(self, nextNode):
        self.key, self.Xm, self.Ym = nextNode.key, nextNode.Xm, nextNode.Ym


class Matrix:
    def __init__(self):
        self.Nodes = []
        self.NodesData = []
        self.sizeX, self.sizeY = 1, 1
        self.size = 1

    def build(self, sizeX, sizeY):
        cordX, cordY = 1, 1
        self.sizeX, self.sizeY = sizeX, sizeY
        self.size = self.sizeX * self.sizeY
        for y in range(self.sizeY):
            for x in range(self.sizeX):
                newNode = MatrixNode(0, cordX, cordY)
                self.Nodes.append(newNode)
                cordX += 1
            cordY += 1
            cordX = 1

    def get(self, x, y):
        if y <= 0 or x <= 0 or y > self.sizeY or x > self.sizeX:
            bufferNode = MatrixNode(0, 0, 0)
            return bufferNode

        return self.Nodes[(y - 1) * self.sizeX + x - 1]

    def find(self, key):
        keyNodes = []
        for node in self.Nodes:
            if node.key == key:
                keyNodes.append(node)

        return keyNodes

    def transmit(self, Matrix):
        for nodeIndex in range(0, len(Matrix.Nodes) - 1):
            self.Nodes[nodeIndex].transmit(Matrix.Nodes[nodeIndex])

    def save(self, name):
        print("Saving...")
        for node in self.Nodes:
            self.NodesData.append(node[0], node[1], node[2])
        matrixF = open((str(name) + ".txt"), "w")
        matrixF.write(repr(self.NodesData))
        matrixF.close()
        print("File saved")

    def load(self, name):
        matrixF = open((str(name) + ".txt"), "r")
        data = matrixF.read()
        matrixF.close()
        data = literal_eval(data)
        loadMatrix = Matrix()
        loadMatrix.NodesData = data
        for node in data:
            newNode = MatrixNode(node[0], node[1], node[2])
            loadMatrix.Nodes.append(newNode)

        loadMatrix.sizeX, loadMatrix.sizeY = data[len(data) - 1][1], data[len(data) - 1][2]
        return loadMatrix