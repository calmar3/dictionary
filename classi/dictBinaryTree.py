# -*- coding: latin -1 -*-
from binaryTree import BinaryNode
from binaryTree import BinaryTree

class DictBinaryTree:
    def __init__(self):
        self.tree=BinaryTree()
    
    def value(self, node):
        if node == None:
            return None
        return node.info[0]
        
    def maxKeySon(self, root):
        curr = root
        while curr.rightSon != None:
            curr = curr.rightSon
        return curr
    
    def search(self,string):
        node = self.searchNode(string)
        return self.value(node)
    
    def find_pred(self,node):
        if (node.leftSon!=None): 
            #cerca il massimo del sottoalbero sinistro 
            pred=self.maxKeySon(node.leftSon)
            if pred!=None:
                return pred
        #oppure sali verso la radice, finchè il nodo corrente non sia il figlio di sinistro di suo padre
        while (node.parent!=None and node.parent.leftSon==node):
            node=node.parent
        return node.parent
    
    
#RICERCA
    
    def searchNode(self,string):
        if self.tree.root!=None:
            c_node=self.tree.root
        else:
            return None
        while c_node!=None:
            if c_node.info[0]==string:
                return c_node
            elif c_node.info[0]<string:
                c_node=c_node.rightSon
            elif c_node.info[0]>string:
                c_node=c_node.leftSon
        return None  
    
#INSERIMENTO

    def insert(self,stringa):    
        #crea un nuovo nodo binario                             
        new_node=BinaryNode([stringa])
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
                        
#CANCELLAZIONE
                                            
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
                        
    # per eliminare un nodo lo scollego in entrambi i versi, cioè scollego il padre dal nodo, ed il nodo dal padre
    def delete_if_noSon(self,node):
        node_to_delete=node
        #verifica se il nodo da rimuovere è la radice
        if self.tree.root==node_to_delete:
            self.tree.root=None
        else:
            pred=node_to_delete.father
            #verifica se il nodo da rimuovere è figlio destro i sinistro del padre, e lo scollega
            if pred.leftSon==node_to_delete:
                pred.leftSon=None
            else:
                pred.rightSon=None
            node_to_delete.father=None
            
    # per eliminare un nodo lo scollego in entrambi i versi, cioè scollego il padre dal figlio, ed il figlio dal padre 
    def delete_if_oneSon(self,node):            
        node_to_delete=node
        #verifica se il nodo da rimuovere è la radice
        if self.tree.root==node_to_delete:
            if node_to_delete.leftSon==None:
                self.tree.root=node_to_delete.rightSon
            else:
                self.tree.root=node_to_delete.leftSon
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
                node_to_delete.father=None      
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
                node_to_delete.father=None
                    

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

        
