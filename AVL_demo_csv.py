#!/usr/bin/env python
# -*- coding: latin-1 -*-
from classi.Parser import parsing
from classi.dictionaryAvl import DictAVL
from classi.Tee import Tee
from time import time
import sys

import math
#import datetime

def demoTest(List,Tree,p1,p2,dim):
    # se la lista non è vuota inserisco gli elementi nell'albero binario          
    p3=1-p1-p2
    #print "La probabilita' p1=",p1," p2=",p2," p3=",p3," e dimensione dell'ordine: ",dim," stringhe\n"
    
    time_tot=0
    if len(List)>0:
        #print "La lista contiene ",len(List)," parole."
        #inserisco gli elementi della lista nell'albero binario
        # inizio il profiling degli inserimenti
        slice_p1=int(math.ceil(len(List)*p1))
        start = time()
        for i in List[:slice_p1]:
            Tree.insert(i)
        # calcolo la differenza di tempo
        elapsed_ins = time() - start
        time_tot=time_tot+elapsed_ins
        
        # ricerco gli elementi della lista
        slice_p2=int(math.ceil(len(List)*p2))
        start=time()
        trovati=0
        for i in List[slice_p1:slice_p1+slice_p2]:
            if(Tree.search(i)):
                trovati=trovati+1
        # calcolo la differenza di tempo
        elapsed_ric = time() - start
        time_tot=time_tot+elapsed_ric
        
        # cancello gli elementi
        slice_p3=int(math.floor(len(List)*p3))
        start=time()
        cancellati=0
        for i in List[slice_p1+slice_p2:slice_p1+slice_p2+slice_p3]:
        #for i in List[:slice_p1]:
            if(Tree.delete(i)):
                cancellati=cancellati+1
        # calcolo la differenza di tempo
        elapsed_can = time() - start
        time_tot=time_tot+elapsed_can
        
        #print "\nTempo di esecuzione totale dell'algoritmo: ",time_tot," s" 
        print len(List),";",p1,";",p2,";",p3,";",elapsed_ins,";",elapsed_ric,";",elapsed_can,";",time_tot
        
if __name__=="__main__":

    list_dim=[5000,10000,15000,20000,25000,30000,35000,40000,45000,50000,1000000]
    MatrixProb = [ [0.3, 0.2], 
                   [0.7, 0.1], 
                   [0.1, 0.7], 
                   [0.4, 0.3] ]
    
    caso="Or"
    #caso="R"
    
#    OutputDir="/Users/Marco/Dropbox/python/Prog4/output_result/"
    OutputDir="/Users/antonio/Dropbox/universita/IA/python/Prog4/output_result/"
    if(OutputDir!=None):
        f = open(OutputDir+"out_result.csv",'a+')
        original = sys.stdout
        sys.stdout = Tee(sys.stdout, f)
        
    print "Alberi AVL - Test ",caso,";;;;;;;"    
    print "n;p1;p2;p3;t_ins;t_ric;t_can;t_tot"
    
    for Dim in range(len(list_dim)-1):
        Dim = list_dim[Dim]
        
        path='txt/'+str(Dim)+str(caso)+'.txt'     
        in_file=open(path,'r')
        text=in_file.read()
        in_file.close()
        l=parsing(text)
        
        for i in range(len(MatrixProb)):
            p1=MatrixProb[i][0]
            p2=MatrixProb[i][1]
    
            b=DictAVL()
            demoTest(l,b,p1,p2,Dim)

    sys.stdout = original
    f.close()