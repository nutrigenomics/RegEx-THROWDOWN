# Import yo' shiznit

import numpy as np
import Bio

from Bio.Phylo.TreeConstruction import DistanceCalculator
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor
from Bio import AlignIO
from Bio import Phylo

import re
import mechanize

# First, we have 5 pre-established files containing the FASTA sequence data of 5 sequences from 5 different
# phylogenetic tree papers. We use 'mechanize' to open page, and will use form filling to feed the optimizer
# the files and extract regexes behind the scenes. Maybe there's a library that can help us with this??

br = mechanize.Browser()
br.open("http://regex.inginf.units.it/")
regex1 = 
regex2 = 
regex3 = 
regex4 = 
regex5 = 
................. more to come


# This is a sample function designed to read in the name of the user's fasta file
# extracted from their regex/resulting sequences

def blosumnj(filename):
    aln = AlignIO.read(open(filename), 'fasta')
    print(aln)

    calculator = DistanceCalculator('blosum62')
    dm = calculator.get_distance(aln)
    print(dm)

    from Bio.Phylo.TreeConstruction import DistanceTreeConstructor
    constructor = DistanceTreeConstructor(calculator, 'nj')
    tree = constructor.build_tree(aln)
    print(tree)
    
# Prompting time! Prompt the users to enter their names, welcome them to the game,
# and then to select their desired set of sequences
    
User1 = (input("\n\nUser 1: Please enter your name:\n\n"))
User2 = (input("\n\nUser 2: Please enter your name:\n\n"))
print(User 1, "and", User 2, "\nWelcome to the REGEX THROWDOWN!\n\n")

print("\nThe objective for this game is to beat your opponent by writing a regular expression whose associated phylogenetic tree most closely matches the phylogenetic tree created by an optimized RegEx created by AI.")

print("\nPlease select which sequence set (based on a phylogenetic tree in a published paper) that you would like to choose for your regex test. Species and name/function of sequence will not be shown.")

print("\nThe blind sequences are as follows:\n1 - Nazli et al.\n2 - Audrey et al.\n3 - Solka et al.\n 4 - Jafri et al.\n5 - Jerome et al.\n\n\n")

sequenceselection = int(input("\n\nPlease enter the number of the sequence set you'd like to choose.\n\n"))

if sequenceselection == 1
    filename = 'fastafile1.fsa'
    else if sequenceselection == 2
        filename = 'fastafile2.fsa'
    else if sequenceselection == 3
        filename = 'fastafile3.fsa'
    else if sequenceselection == 4
        filename = 'fastafile4.fsa'
    else if sequenceselection == 5
        filename = 'fastafile5.fsa'
    else
        print("I'm sorry! You need to enter a number between 1 and 5 to indicate your chosen set of sequences. Try again!")
        sequenceselection = int(input("\n\nPlease enter the number of the sequence set you'd like to choose.\n\n"))    

# Prompt the users to enter their best RegEx guesses

User1Regex = (input("\n\nUser 1: Please enter your best guess RegEx.:\n\n"))
User2Regex = (input("\n\nUser 2: Please enter your best guess RegEx.:\n\n"))

# The following code block will enter each of the users' RegEx (User1Regex and User2Regex) either as a search term
# within ProSite's downloaded file OR on the ProSite/Expasy site iself

##### IN THIS CODE BLOCK WE WILL TAKE USER REGEX INPUT, SEARCH PROSITE, AND USE THE RESULTING NUMBERS TO
##### GENERATE A FASTA FILE.

    # ******** I need to read more on mechanize or other libraries to determine how to proceed to extract ********
    # ******** those UniProt ID numbers from the search results                                           ********
    
    # One promising library: https://github.com/biopython/biopython/blob/master/Bio/ExPASy/ScanProsite.py
    
    # PROPOSED STRATEGY to convert search results to FSA files:
    
    # Sample Uniprot search format https://www.uniprot.org/uniprot/?query=SEQ1ID+OR+SEQ2ID+OR+SED3ID+OR+SEQ4ID+OR+SEQ5ID&sort=score
    # Sample Uniprot search FASTA result with SEQ1ID,SEQ2ID, etc., limited to first 5 results:
    # https://www.uniprot.org/uniprot/?query=SEQ1ID%20OR%20SEQ2ID%20OR%20SEQ3ID%20OR%20%20SEQ4ID%20OR%20SEQ5ID&format=fasta&limit=5&sort=score
    
    # So what we do, is find a way to extract the top 5 uniprot ids from the prosite motif results, and we store
    # the results of those IDs in 5 variables: SEQ1ID, SEQ2ID, etc. (Only the uniprot code instead of these IDs)
    
    # Then we write a string that is the above Uniprot search result that includes those variable names,
    # and extract the website's text, which we then save into a FASTA .fsa file. I might need to try a few
    # different ways to successfully create that link. This is all just sketched draft code.
    
    import bs4
    import urllib.request
    
    link = ('https://www.uniprot.org/uniprot/?query=',SEQ1ID,'%20OR%20',SEQ2ID,'%20OR%20',SEQ3ID,'%20OR%20%20',SEQ4ID,'%20OR%20%20',SEQ5ID,'&format=fasta&limit=5&sort=score')

    soup = bs4.BeautifulSoup(webpage)
    
    print("Here is the FASTA file created from the top 5 sequence results generated when your RegEx was run through Scan Prosite's motif search:")
    print(soup.get_text())
    
    # ******* Insert code block to save the extracted web page text as .fsa file. *******
    # ******* I think we can do this with BioPython's SeqIO?                      *******
    
    # ******* Insert code block to length-equalize the sequences in the .fsa file you just created: *******
    # ******* https://www.biostars.org/p/185103/                                                    *******

    # This same block of text will extract the uniprot name and/or fasta sequence for the top 5 results.
    # We may be able to recruit an existing Python library for that purpose, so we should search a little before hand-coding.

    # We also need to find a Python library or tool to generate FASTA files out of subblock A. We will need to
    # determine how to equalize the sequences in length, as well, since the BioPython code will not run on sequences of
    # unequal length
    
# Now, we run our blosumnj function on the Regex FASTA file, and the FASTA files we just generated
# through the users' regexes.

# First create the tree based upon 'filename', which was generated based upon user input of desired sequence

blosumnj(filename)

# Assign the matrix variable from the function just run to the variable 'exampledm'. Store the tree similarly.

exampledm = dm
exampletree = tree

print("Here is the sample distance matrix created with the optimzed RegEx:\n\n", exampledm,"\n\n")
print("Here is the tree that results from this sample distance matrix:\n\n", exampletree,"\n\n")

# Now run the blosumnj function on the User 1 FASTA file

blosumnj(user1filename)

user1dm = dm
user1tree = tree

print("Here is", User1,"'s distance matrix:\n\n", user1dm,"\n\n")
print("Here is", User1,"'s tree:\n\n", user1tree,"\n\n")

# Now run the blosumnj function on the User 2 FASTA file

blosumnj(user2filename)

user2dm = dm
user2tree = tree

print("Here is", User2,"'s distance matrix:\n\n", user2dm,"\n\n")
print("Here is", User2,"'s tree:\n\n", user2tree,"\n\n")

# Now it is time to score the trees accordingly

print("It's time to compare and score the players' trees against the optimized RegEx tree!\n\nFirst, we will see if all species are the same.")

    # This is where I need some library or other tool or example to figure out how to extract the information from the matrices and trees
    # Potential tool: https://github.com/biologyguy/BuddySuite/wiki/PB-Show-unique to show differences between trees, species-wise

def score(phylogeny):
    
    # Here just basically an 'if' loop that matches the species in the RegEx tree with those in the user tree. Basic scoring structure.
    
    # Another loop that somehow accounts for accuracy of clustering together, if possible.
    
    # Sum scores, print statement of the score for that user

phylogeny = user1tree
score(user1tree)
user1score = score

phylogeny = user2tree
score(user2tree)
user2score = score

if user1score>user2score
    winner = User1
    print(User1"'s regex score is," user1score,"! "User2"'s RegEx score is," user2score,"! ", User1, "you CRUSHED THE COMPETITION! LET THE BRAGGING RIGHTS COMMENCE!\n\n")
        else if user2score>user1score
            winner = User2
            print(User2"'s regex score is," user2score,"! "User1"'s RegEx score is," user1score,"! ", User2, "you CRUSHED THE COMPETITION! LET THE BRAGGING RIGHTS COMMENCE!\n\n")

    # OR: Another VERY promising comparison tool that seems to do it all: http://etetoolkit.org/documentation/ete-compare/
    # http://etetoolkit.org/docs/latest/tutorial/tutorial_phylogeny.html?highlight=fasta#linking-phylogenetic-trees-with-multiple-sequence-alignments
                       
print(winner,", YOU GET TO VICTORY DANCE WITH CARLTON!")
br.open("https://youtu.be/Lxqa2Haf8lo?t=19")