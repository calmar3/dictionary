# -*- coding: latin-1 -*-
class BinaryNode:
    def __init__(self, info=[]):
        self.info = info    #lista [chiave] 
        self.father = None
        self.leftSon = None
        self.rightSon = None

class BinaryTree:
    
    def __init__(self, rootNode=None):
        self.root = rootNode    
    
    def insertAsLeftSubTree(self, father, subtree):
        son = subtree.root
        if son != None:
            son.father = father
        father.leftSon = son
    
    def insertAsRightSubTree(self, father, subtree):
        son = subtree.root
        if son != None:
            son.father = father
        father.rightSon = son

    def cutLeft(self, father):
        son = father.leftSon
        newTree = BinaryTree(son)
        father.leftSon = None
        return newTree
    
    def cutRight(self, father):
        son = father.rightSon
        newTree = BinaryTree(son)
        father.rightSon = None
        return newTree
    
    
