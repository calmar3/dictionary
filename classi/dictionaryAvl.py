# -*- coding: latin-1 -*-
from binaryTree import BinaryTree
from binaryTree import BinaryNode
from dictBinaryTree import DictBinaryTree

class DictAVL(DictBinaryTree):
    def __init__(self):
        self.tree=BinaryTree()  #I nodi ora sono una lista [chiave,altezza]
    
    def height(self,node):
        if node==None:
            return -1
        return node.info[1]
    
    def setHeight(self,node,h):
        if node!=None:
            node.info[1]=h
    
    def balanceFactor(self,node):
        if node==None:
            return 0
        return self.height(node.leftSon)-self.height(node.rightSon)

    def updateHeight(self,node):
        if node!=None:
            self.setHeight(node,max(self.height(node.leftSon),self.height(node.rightSon))+1)

#BILANCIAMENTO

    def rightRotation(self,node):
        leftSon=node.leftSon
        node.info,leftSon.info=leftSon.info,node.info
        
        rtree=self.tree.cutRight(node)
        ltree=self.tree.cutLeft(node)
        ltree_l=ltree.cutLeft(leftSon)
        ltree_r=ltree.cutRight(leftSon)
        
        ltree.insertAsRightSubTree(ltree.root, rtree)
        ltree.insertAsLeftSubTree(ltree.root, ltree_r)
        self.tree.insertAsRightSubTree(node, ltree)
        self.tree.insertAsLeftSubTree(node, ltree_l)
        
        self.updateHeight(node.rightSon)
        self.updateHeight(node)
    
    def leftRotation(self,node):
        rightSon=node.rightSon        
        node.info,rightSon.info=rightSon.info,node.info
        
        rtree=self.tree.cutRight(node)
        ltree=self.tree.cutLeft(node)
        rtree_l=rtree.cutLeft(rightSon)
        rtree_r=rtree.cutRight(rightSon)
        
        rtree.insertAsLeftSubTree(rtree.root, ltree)
        rtree.insertAsRightSubTree(rtree.root, rtree_l)
        self.tree.insertAsLeftSubTree(node, rtree)
        self.tree.insertAsRightSubTree(node, rtree_r)
        
        self.updateHeight(node.leftSon)
        self.updateHeight(node)

    def rotate(self,node):
        balFact=self.balanceFactor(node)
        #controlla il fattore di bilanciamento per scegliere la rotazione opportuna
        if balFact==2:
            if self.balanceFactor(node.leftSon)>=0:
                self.rightRotation(node)
            else:
                self.leftRotation(node.leftSon)
                self.rightRotation(node)
        elif balFact==-2:
            if self.balanceFactor(node.rightSon)<=0:
                self.leftRotation(node)
            else:
                self.rightRotation(node.rightSon)
                self.leftRotation(node)
        
#INSERIMENTO

    def balInsert(self,newNode):
        curr=newNode.father
        while curr!=None:
            if abs(self.balanceFactor(curr))>=2:
                break #smette di aggiornare le altezze appena trova un nodo da ruotare 
            else:
                self.updateHeight(curr)
                curr=curr.father
        if curr!=None:
            self.rotate(curr)
    
    def insert(self,stringa):    
        #crea un nuovo nodo binario                             
        new_node=BinaryNode([stringa,0])
        #verifica se l'albero è vuoto
        if self.tree.root==None: 
            self.tree.root=new_node
        else:
            current_node=self.tree.root
            inserted=False
            while inserted==False:
                if new_node.info[0]<=current_node.info[0]: 
                    if current_node.leftSon==None:
                        new_node.father=current_node
                        current_node.leftSon=new_node
                        inserted=True
                    else:
                        current_node=current_node.leftSon
                else:
                    if current_node.rightSon==None:
                        new_node.father=current_node
                        current_node.rightSon=new_node
                        inserted=True
                    else:
                        current_node=current_node.rightSon
        self.balInsert(new_node)                  

#CANCELLAZIONE: 

    def balDelete(self,removedNode):
        curr=removedNode.father
        while curr!=None: 
            #ribilanciamento e modifica altezza a seguito della cancellazione
            if abs(self.balanceFactor(curr))==2:
                self.rotate(curr)
            else:
                self.updateHeight(curr)
            curr=curr.father

    def delete(self,stringa):
        #verifico se il il nodo che devo eliminare esiste nell'albero
        node_to_delete=self.searchNode(stringa)                           
        if node_to_delete!=None: 
            #se il nodo che cerco è presente ho tre casi
            if node_to_delete.rightSon==None and node_to_delete.leftSon==None:
                self.delete_if_noSon(node_to_delete)
                return True
            elif node_to_delete.rightSon==None or node_to_delete.leftSon==None:
                self.delete_if_oneSon(node_to_delete)
                return True
            else:
                self.delete_if_twoSon(node_to_delete)
                return True
        return None
                      
# per eliminare un nodo lo scollego in un solo verso, cioè scollego il padre dal figlio, non il figlio dal padre, collegamento utile nella rotazione
    def delete_if_noSon(self,node):
        node_to_delete=node
        #verifica se il nodo da rimuovere è la radice
        if self.tree.root==node_to_delete:
            self.tree.root=None
            return
        else:
            pred=node_to_delete.father
            #verifica se il nodo da rimuovere è figlio destro i sinistro del padre, e lo scollega
            if pred.leftSon==node_to_delete:
                pred.leftSon=None
            else:
                pred.rightSon=None
        self.balDelete(node_to_delete)#ribilancia

# per eliminare un nodo lo scollego in un solo verso, cioè scollego il nodo dal figlio, non il figlio dal nodo
# collegamento utile nella rotazione
    def delete_if_oneSon(self,node):            
        node_to_delete=node
        #verifica se il nodo da rimuovere è la radice
        if self.tree.root==node_to_delete:
            if node_to_delete.leftSon==None:
                self.tree.root=node_to_delete.rightSon
                node_to_delete.rightSon=None
            else:
                self.tree.root=node_to_delete.leftSon
                node_to_delete.leftSon=None
            self.tree.root.father=None
            
        else:
            pred=node_to_delete.father
            #verifica se l'unico figlio del nodo da eliminare è il destro o il sinistro
            if node_to_delete.leftSon==None:
                rs=node_to_delete.rightSon
                #verifica se il nodo da cancellare è figlio destro o sinistro del padre
                if pred.leftSon==node_to_delete:
                    pred.leftSon=rs                         
                elif pred.rightSon==node_to_delete:
                    pred.rightSon=rs
                rs.father=pred        
                node_to_delete.rightSon=None                 
            elif node_to_delete.rightSon==None:
                ls=node_to_delete.leftSon
                #verifica se il nodo da cancellare è figlio destro o sinistro del padre
                if pred.leftSon==node_to_delete:
                    pred.leftSon=ls
                elif pred.rightSon==node_to_delete:
                    pred.rightSon=ls
                ls.father=pred
                node_to_delete.leftSon=None
        self.balDelete(node_to_delete)#ribilancia 
                    

    def delete_if_twoSon(self,node):
        node_to_delete=node
        #cerca il predecessore
        pred=self.find_pred(node_to_delete)
        pred.info,node_to_delete.info=node_to_delete.info,pred.info
        #verifica se il nodo nella nuova posizione ha uno o zero figli
        if pred.rightSon==None and pred.leftSon==None:
            self.delete_if_noSon(pred)
        elif pred.rightSon==None or pred.leftSon==None:
            self.delete_if_oneSon(pred) 