# -*- coding: latin -1 -*-

#importiamo il modulo delle espressioni regolari
import re

def parsing (text):
# definiamo la funzione parsing alla quale passiamo come argomento una stringa di testo
# la funzione restituisce una lista contenente solo le parole che risultano coincidere con i criteri
# definiti nell'espressione regolare
#
# Il criterio \w+ filtra solo le parole
    text=text.lower()
    return re.findall(r"[\w]+",text,re.UNICODE)

    
        
    