#!/usr/bin/env python
# -*- coding: latin-1 -*-
import os
import sys

class Progetto:
    
    def __init__(self):
        # attributo inizializzato con la posizioine assoluta dello script PROGETTO_4 
        self.OutputPath = self.getPathProgetto()+'/output_result/'
        self.Sorted = False #usata per definire il caso di ordinamento 
        self.p1 = 0 # probabilita' p1 usata per gli inserimenti
        self.p2 = 0 # probabilita' p2 usata per le ricerche
        self.list_dim=[5000,10000,15000,20000,25000,30000,35000,40000,45000,50000,200000] #lista contenente le dimensioni delle istanze di inpute
        self.dim = self.list_dim[0] # scelta di default come prima istanza di input
    
    def getPathProgetto(self):     
        # restituisce il path assoluto del progetto       
        pathname = os.path.dirname(sys.argv[0])        
        return os.path.abspath(pathname)
        
    def setInitial(self):
        # metodo per l'assegnazione e la validazione delle probabilita' e della dimensione dell'istanza di input
        self.p1 = input("Inserire la prob p1 (inserimento):\n")
        if self.p1<0 or self.p1>1:
            print "Controllare le probabilita' inserite!\n"
            return False
        self.p2 = input("Inserire la prob p2 (ricerca):\n")
        if self.p2<0 or self.p2>1:
            print "Controllare le probabilita' inserite!\n"
            return False
        p3 = 1-self.p1-self.p2
        if (p3<0 or p3>1):
            print "Controllare le probabilita' inserite!\n"
            return False
        print self.list_dim,"\n(NB: la dimensione 200000 e' un test aggiuntivo funzionante solo nel caso random)\n"
        self.dim = input("Seleziona la dimensione di input:\n")
        if self.dim not in self.list_dim:
            print "Dimensione non corretta!\n"
            return False
        return True
         
    def setSorting(self,sorting):
        # imposta il caso di ordinamento
        self.Sorting= sorting
    
    def setOutputPath(self,Path):
        # controlla che il percorso passato per argomento termini con il carattere /
        if Path[-1:]!='/':
            Path+='/'
        self.OutputPath = Path
    
    def printMainMenu(self,doClean=1):
        # cancello lo schermo
        if doClean:
            self.clearScreen()
        # stampo il menu principale
        print " Menu:\n"
        print "\t1) Alberi binari di ricerca\n"
        print "\t2) Alberi AVL\n"
        print "\t3) Imposta path di Output\n"
        print "\t4) Apri file relazione (PDF)\n"
        print "\t5) Chiudi Progetto\n"
        
    def printSubMenu1(self,doClean=1):
        #cancello lo schermo
        if doClean:
            self.clearScreen()
        # stampo il menu secondario
        print " Menu Alberi Binari di Ricerca:\n"
        print "\t1) AVVIA TEST Random\n"
        print "\t2) AVVIA TEST Sequenze Ordinate\n"
        print "\t3) Torna al MENU PRINCIPALE\n"
        
    def printSubMenu2(self,doClean=1):
        #cancello lo schermo
        if doClean:
            self.clearScreen()
        # stampo il menu secondario
        print " Menu AVL:\n"
        print "\t1) AVVIA TEST Random\n"
        print "\t2) AVVIA TEST Sequenze Ordinate\n"
        print "\t3) Torna al MENU PRINCIPALE\n"
    
        
    def clearScreen(self):
        # metodo per la cancellazione del contenuto a schermo, diversificato per i vari SO
        numlines = 100
        if os.name == "posix":
            # Unix/Linux/MacOS/BSD/etc
            os.system('clear')
        elif os.name in ("nt", "dos", "ce"):
            # DOS/Windows
            os.system('CLS')
        else:
            # Fallback for other operating systems.
            print '\n' * numlines
        
if __name__ == "__main__":
    progetto4 = Progetto()
    print "\tProgetto 4: Alberti binari di ricerca e alberi AVL\n"

    progetto4.printMainMenu()
    option = 0
    while not option == 5:
        option = input(' Scegli un opzione:\n')
        if option ==1:
            progetto4.printSubMenu1()
            while not option == 3:
                option = input(' Scegli un opzione:\n') 
                if option ==1:
                    progetto4.clearScreen()
                    if progetto4.setInitial():
                        progetto4.Sorted=False
                        sys.argv = [progetto4.p1, progetto4.p2, progetto4.dim, progetto4.OutputPath,progetto4.Sorted]
                        execfile('BST_demo.py')
                    progetto4.printSubMenu1(0)
                elif option ==2:
                    progetto4.clearScreen()
                    if progetto4.setInitial():
                        progetto4.Sorted=True
                        sys.argv = [progetto4.p1, progetto4.p2, progetto4.dim, progetto4.OutputPath,progetto4.Sorted]
                        execfile('BST_demo.py')
                    progetto4.printSubMenu1(0)
                elif option == 3:
                    progetto4.printMainMenu()
        elif option==2:
            progetto4.printSubMenu2()
            while not option == 3:
                option = input(' Scegli un opzione:\n') 
                if option ==1:
                    progetto4.clearScreen()
                    if progetto4.setInitial():
                        progetto4.Sorted=False
                        sys.argv = [progetto4.p1, progetto4.p2, progetto4.dim, progetto4.OutputPath,progetto4.Sorted]
                        execfile('AVL_demo.py')
                    progetto4.printSubMenu2(0)
                elif option ==2:
                    progetto4.clearScreen()
                    if progetto4.setInitial():
                        progetto4.Sorted=True
                        sys.argv = [progetto4.p1, progetto4.p2, progetto4.dim, progetto4.OutputPath,progetto4.Sorted]
                        execfile('AVL_demo.py')
                    progetto4.printSubMenu2(0)
                elif option == 3:
                    progetto4.printMainMenu()
        elif option==3:
            OutDir = raw_input("Inserire il percorso completo:\n")
            progetto4.setOutputPath(OutDir)
            progetto4.printMainMenu(1)
        elif option==4:
            print "Apro PDF relazione"
            if sys.platform.startswith('darwin'):
			    os.system('open Relazione.pdf')
            elif sys.platform.startswith('linux'):
                os.system('xdg-open Relazione.pdf')
            elif sys.platform.startswith('win32'):
                os.startfile('Relazione.pdf')
        elif option==5:
            progetto4.clearScreen()
            print "Termino il progetto\n"
            # chiamata di sistema per terminare lo script
            sys.exit()