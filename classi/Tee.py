# -*- coding: latin-1 -*-
import  os,sys

class Tee(object):
    def __init__(self, *files):
    	# ricevo un elenco di argomenti e li memorizzo nell'attributo files
        self.files = files
    def write(self, obj):
    	# scrivo obj in ogni elemento di files (nel nostro caso il puntatore al file e il sys.stdout)
        for f in self.files:
            f.write(obj)
