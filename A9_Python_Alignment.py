#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 10:44:18 2019

@author: nazli
"""
#FOR A9 SUBSECTION 
#Importing the Clustal Omega Tool 
from Bio.Align.Applications import ClustalOmegaCommandline 
from Bio import Phylo
from Bio import AlignIO 
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor
from Bio.Phylo.TreeConstruction import DistanceCalculator


#The input file of the FASTA sequences 

Input_file= "/Users/nazli/Downloads/Sequence.txt"

#The output file specification 

output_file= "aligned.fasta" 

#The command for running ClustalOmega 

clustalomega_cline= ClustalOmegaCommandline(infile= Input_file, outfile= output_file, verbose= True, auto= True )

print (clustalomega_cline)

align=AlignIO.read("/users/nazli/Downloads/aligned.fasta","fasta")
print(align)

calculator=DistanceCalculator('identity')
Main=calculator.get_distance(align)
Main
print(Main)

constructor= DistanceTreeConstructor()
tree=constructor.nj(Main)
print(tree) 
Phylo.draw(tree)


