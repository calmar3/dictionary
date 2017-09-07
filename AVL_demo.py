#!/usr/bin/env python
# -*- coding: latin-1 -*-
from classi.Parser import parsing
from classi.Tee import Tee
from classi.dictionaryAvl import DictAVL
from time import time
import sys
import math
import datetime

def demoTest(List,Tree,p1,p2,dim):
    # se la lista non è vuota inserisco gli elementi nell'albero binario      
    p3=1-p1-p2
    print "La probabilita' p1=",p1," p2=",p2," p3=",p3," e dimensione dell'ordine: ",dim," stringhe\n"
    time_tot=0
    if len(List)>0:
        print "La lista contiene ",len(List)," parole."
        #inserisco gli elementi della lista nell'albero binario
        # inizio il profiling degli inserimenti
        slice_p1=int(math.ceil(len(List)*p1))
        start = time()
        for i in List[:slice_p1]:
            Tree.insert(i)
        # calcolo la differenza di tempo
        elapsed = time() - start
        print "Tempo speso per inserimento di ",slice_p1," elementi : ",elapsed,"s."
        time_tot=time_tot+elapsed
        
        # ricerco gli elementi della lista
        slice_p2=int(math.ceil(len(List)*p2))
        start=time()
        trovati=0
        for i in List[slice_p1:slice_p1+slice_p2]:
            if(Tree.search(i)):
                trovati=trovati+1
        # calcolo la differenza di tempo
        elapsed = time() - start
        print "Tempo speso per la ricerca di ",slice_p2," elementi : ",elapsed,"s."," - Occorrenze: ",trovati
        time_tot=time_tot+elapsed
        
        # cancello gli elementi
        slice_p3=int(math.floor(len(List)*p3))
        start=time()
        cancellati=0
        for i in List[slice_p1+slice_p2:slice_p1+slice_p2+slice_p3]:
        #for i in List[:slice_p1]:
            if(Tree.delete(i)):
                cancellati=cancellati+1
        # calcolo la differenza di tempo
        elapsed = time() - start
        print "Tempo speso per la cancellazione di ",slice_p3," elementi : ",elapsed,"s."," - Elementi cancellati: ",cancellati
        time_tot=time_tot+elapsed
        
        print "\nTempo di esecuzione totale dell'algoritmo: ",time_tot," s"   
        
if __name__=="__main__":
    
    Dim = sys.argv[2]
    if(sys.argv[4]==True):
        caso="Or"
    else:
        caso="R"
    path='txt/'+str(Dim)+str(caso)+'.txt'     
    in_file=open(path,'r')
    text=in_file.read()
    in_file.close()
    l=parsing(text)
    
    OutputDir=sys.argv[3]
    if(OutputDir!=None):
        try:
            f = open(OutputDir+"out_result.txt",'a+')
            original = sys.stdout
            sys.stdout = Tee(sys.stdout, f) 
        
            print "----------------------------------------------------------------" 
            now = datetime.datetime.now()
            print "Inizio test: ", now.strftime("%Y-%m-%d %H:%M:%S")  
            if(sys.argv[4]==True):
                print "\nAlberi AVL - TEST SEQUENZE ORDINATE\n"
            else:
                print "\nAlberi AVL -  TEST RANDOM\n"
        
            b=DictAVL()
            demoTest(l,b,sys.argv[0],sys.argv[1],Dim)
            
            now = datetime.datetime.now()
            print "Termine test: ", now.strftime("%Y-%m-%d %H:%M:%S"),"\n"
            print "----------------------------------------------------------------" 
            sys.stdout = original
            f.close() 
            
        except IOError as e:
            print "\nErrore nella scrittura del file dei risultati\n\nControllare la correttezza del path di output"    
        