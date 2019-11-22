#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 12:02:24 2019

@author: nazli
"""
#FOR A9 SUBSECTION 
from Bio import Phylo
from Bio import AlignIO 
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor
from Bio.Phylo.TreeConstruction import DistanceCalculator

align=AlignIO.read("/users/nazli/Desktop/aln-clustal_num.clustal_num","clustal")
print(align)

calculator=DistanceCalculator('identity')
Main=calculator.get_distance(align)
Main
print(Main)

constructor= DistanceTreeConstructor()
tree=constructor.nj(Main)
print(tree) 
Phylo.draw(tree)
