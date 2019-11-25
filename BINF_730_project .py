#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Import BeautifulSoup and use it to open the Prosite Web Page.
# Feel free to use P-x(2)-G-E-S-G(2)-[AS] as your sample pattern.

from bs4 import BeautifulSoup

# Import other stuff

import re
import requests

import Bio
from Bio.Phylo.TreeConstruction import DistanceCalculator
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor
from Bio import AlignIO
from Bio import Phylo

homedir = input("Please specify your home directory for Python file execution/FASTA file storage: ")


User1 = input("\nUSER 1: Please enter your name: ")
User2 = input("\nUSER 2: Please enter your name: ")

print("\n\nWelcome", User1," and", User2,"TO REGEX THROWDOWN!\n\n")

print("This game allows 2 users to test their regular expression writing skills.\n")
print("We have used a standardized consensus pattern generator to write consensus patterns\nbased on gene sets featured in phylogenetic trees in published literature.\n")
print("These consensus patterns were then used to search ProSite and construct phylogenetic\ntrees based on the top 5 resulting gene sequence matches.\n")
print("Your goal is to examine the sequence alignment from the gene set you choose, and write\n a consensus pattern whose resulting phylogenetic tree is closer to the original than your opponent's tree!")

geneselection = input("\n\nFirst, select a gene set for this round. \nPlease type A for Franchini and Elgoyen (2006), B for Author and Author (Year), and C for Author and Author (Year).\n\n")

if geneselection == "A":
    regexselection = "Q-V-V-D-x-E"
elif geneselection == "B":
    regexselection = "B-B-B-B-B"
elif geneselection == "C":
    regexselection = "C-C-C-C-C-C"
else:
    print ("I'm sorry, you will need to select a set using the letters A, B, or C.")
    geneselection = input("\n\nFirst, select a gene set for this round. Please type A for Franchini and Elgoyen (2006), B for Author and Author (Year), and C for Author and Author (Year).\n\n")

print("\n\n\n")
    
print (User1,", RISE TO THE OCCASION!")
regex1 = input("Enter your ProSite formatted pattern: ")
print (User2,", LET'S DO THIS!")
regex2 = input("Enter your ProSite formatted pattern: ")

url1 = "https://prosite.expasy.org/cgi-bin/prosite/PSScan.cgi?sig="+regex1
url2 = "https://prosite.expasy.org/cgi-bin/prosite/PSScan.cgi?sig="+regex2
# Processing the standardized regex with dynamic programming
urlselection = "https://prosite.expasy.org/cgi-bin/prosite/PSScan.cgi?sig="+regexselection


r1  = requests.get(url1)
r2  = requests.get(url2)
rselection = requests.get(urlselection)

data1 = r1.text
data2 = r2.text
dataselection = rselection.text

soup1 = str(BeautifulSoup(data1))
soup2 = str(BeautifulSoup(data2))
soupselection = str(BeautifulSoup(dataselection))


#print("\n*********************\n\nHere are the Prosite search results based on your regular expression:\n*********************\n\n")
#print(soup)
#print("\n\n\nNow, we will scrape the results for the top 5 gene results, while ignoring isoforms.\n\n")

# Importing the regular expression library and asking it to find all gene name formatted matches in the Prosite content,
# while ignoring isoforms, so that we don't have duplicates

import re

#souplist = re.findall(r"\|[a-zA-Z0-9]*?[\-]*?[a-zA-Z0-9]*?[\-|\|]", soup)

souplist1 = re.findall(r"\|[a-zA-Z0-9]*?\|", soup1)
souplist2 = re.findall(r"\|[a-zA-Z0-9]*?\|", soup2)
souplistselection = re.findall(r"\|[a-zA-Z0-9]*?\|", soupselection)


# Delete the last two entries which are "||" from the HTML of that same webpage.
    
del souplist1[-1]
del souplist1[-1]
del souplist2[-1]
del souplist2[-1]
del souplistselection[-1]
del souplistselection[-1]


# Strip out | and - which were initially kept as part of the regular expression to isolate gene names

striplist1 = ([s.replace('|', '') for s in souplist1]) # remove the | from the string borders
striplist1 = ([s.replace('-', '') for s in striplist1])

striplist2 = ([s.replace('|', '') for s in souplist2]) # remove the | from the string borders
striplist2 = ([s.replace('-', '') for s in striplist2])

striplistselection = ([s.replace('|', '') for s in souplistselection]) # remove the | from the string borders
striplistselection = ([s.replace('-', '') for s in striplistselection])

print("\n\n\n")

print("\n\nUSER 1: Here is the list of genes matched by ", User1,"'s submitted ProSite pattern, ignoring isoforms. \nWe will be using only the first 5 best matches to construct your phylogenetic tree.\n\n")
for gene1 in striplist1:
    print(gene1)
    
print("\n\nUSER 2: Here is the list of genes matched by ", User2,"'s submitted ProSite pattern, ignoring isoforms. \nWe will be using only the first 5 best matches to construct your phylogenetic tree.\n\n")
for gene2 in striplist2:
    print(gene2)
    
print("\n\nMEANWHILE, here is the list of genes matched by the standard ProSite consensus pattern, ignoring isoforms. \nWe will be using only the first 5 best matches to construct your phylogenetic tree.\n\n")
for geneselection in striplistselection:
    print(geneselection)
    
print("\n\nCan you already guess just by looking at the sequences who might be the winner?\n")
    
print("\n\n\n")

proceed = input("Please enter, 'Y' when ready to proceed with creation of alignments, distance matrices, and phylogenetic trees!")

# Assign a variable to the first 5 results in the list of resulting genes
    
User1Seq1 = striplist1[0]
User1Seq2 = striplist1[1]
User1Seq3 = striplist1[2]
User1Seq4 = striplist1[3]
User1Seq5 = striplist1[4]
    
User2Seq1 = striplist2[0]
User2Seq2 = striplist2[1]
User2Seq3 = striplist2[2]
User2Seq4 = striplist2[3]
User2Seq5 = striplist2[4]

Selection1 = striplistselection[0]
Selection2 = striplistselection[1]
Selection3 = striplistselection[2]
Selection4 = striplistselection[3]
Selection5 = striplistselection[4]

# Concatenate the User1 sequences into the uniprot.org FASTA formatted link, and open it in a new window,
# to demonstrate the FASTA formatted sequences
    
fastalink1 = ('https://www.uniprot.org/uniprot/?query='+User1Seq1+'%20OR%20'+User1Seq2+'%20OR%20'+User1Seq3+'%20OR%20%20'+User1Seq4+'%20OR%20%20'+User1Seq5+'&format=fasta&limit=5&sort=score')
fastalink2 = ('https://www.uniprot.org/uniprot/?query='+User2Seq1+'%20OR%20'+User2Seq2+'%20OR%20'+User2Seq3+'%20OR%20%20'+User2Seq4+'%20OR%20%20'+User2Seq5+'&format=fasta&limit=5&sort=score')
fastalinkselection = ('https://www.uniprot.org/uniprot/?query='+Selection1+'%20OR%20'+Selection2+'%20OR%20'+Selection3+'%20OR%20%20'+Selection4+'%20OR%20%20'+Selection5+'&format=fasta&limit=5&sort=score')

import webbrowser

# Optional: webbrowser.open_new(fastalink)

# NEXT STEP: Write the content of the above link to a txt FASTA file
# Using Beautiful Soup to do this!

r1  = requests.get(fastalink1)
r2  = requests.get(fastalink2)
rselection = requests.get(fastalinkselection)

data1 = r1.text
data2 = r2.text
dataselection = rselection.text

user1soup = str(BeautifulSoup(data1))
user2soup = str(BeautifulSoup(data2))
selectionsoup = str(BeautifulSoup(dataselection))

user1soup = re.sub('<html><head></head><body>', '', user1soup)
user1soup = re.sub('</body></html>', '', user1soup)
user1soup = re.sub('&gt;', '>', user1soup)
user2soup = re.sub('<html><head></head><body>', '', user2soup)
user2soup = re.sub('</body></html>', '', user2soup)
user2soup = re.sub('&gt;', '>', user2soup)
selectionsoup = re.sub('<html><head></head><body>', '', selectionsoup)
selectionsoup = re.sub('</body></html>', '', selectionsoup)
selectionsoup = re.sub('&gt;', '>', selectionsoup)

print("\n\nHere are your top 5 matched sequences in FASTA format, ", User1,":\n")
print(user1soup)

print("\n\nHere are your top 5 matched sequences in FASTA format, ", User2,":\n")
print(user2soup)

    
print("\nNow we will use each of", User1,"'s and", User2,"'s FASTA sequence sets to generate:\n ~ a multiple sequence alignment\n ~ a distance matrix, and\n ~ a phylogenetic tree!")


text_file = open("User1FASTA.fsa", "w")
n = text_file.write(user1soup)
text_file.close()

text_file = open("User2FASTA.fsa", "w")
n = text_file.write(user2soup)
text_file.close()

text_file = open("Selection.fsa", "w")
n = text_file.write(selectionsoup)
text_file.close()


#Importing the modules for MSA, Distances Matrices, and Tree Building 
from Bio.Align.Applications import ClustalOmegaCommandline 
from Bio import Phylo
from Bio import AlignIO 
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor
from Bio.Phylo.TreeConstruction import DistanceCalculator


#The input file of the FASTA sequences 

Input_file1= User1FASTA.fsa
Input_file2= User2FASTA.fsa

#The output file specification 

output_file1= "user1_aligned.fasta" 
output_file2= "user2_aligned.fasta"

#The command for running ClustalOmega 

clustalomega_cline1= ClustalOmegaCommandline(infile= Input_file1, outfile= output_file1, verbose= True, auto= True )
print (clustalomega_cline1)
print ("User 1, please Enter the Following command in the Terminal:./clustalo -i /Users/nazli/Downloads/Sequence.txt -o user1_aligned.fasta --auto -v")
clustalomega_cline2= ClustalOmegaCommandline (infile= Input_file2, outfile= output_file2, verbose= True, auto= True)
print (clustalomega_cline2)
print ("User 2, please Enter the Following command in the Terminal:./clustalo -i /Users/nazli/Downloads/Sequence.txt -o user2_aligned.fasta --auto -v")

align1=AlignIO.read("/Users/nazli/Downloads/user1_aligned.fasta","fasta")
align2=AlignIO.read ("/Users/nazli/Downloads/user2_aligned.fasta", "fasta")
print(align1)
print (align2)

calculator=DistanceCalculator('identity')
Main1=calculator.get_distance(align1)
Main1
print(Main1)

calculator=DistanceCalculator('identity')
Main2=calculator.get_distance(align2)
Main2
print(Main2)

constructor= DistanceTreeConstructor()
tree1=constructor.nj(Main1)
print(tree1) 
Phylo.draw(tree1)

constructor= DistanceTreeConstructor()
tree2=constructor.nj(Main2)
print(tree2) 
Phylo.draw(tree2)
