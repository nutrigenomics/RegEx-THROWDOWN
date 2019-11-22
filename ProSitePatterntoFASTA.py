# Import BeautifulSoup and use it to open the Prosite Web Page. Feel free to use P-x(2)-G-E-S-G(2)-[AS] as your sample pattern.

from bs4 import BeautifulSoup

import requests

import re

regex1 = input("USER 1: Enter your ProSite formatted pattern: ")

url1 = "https://prosite.expasy.org/cgi-bin/prosite/PSScan.cgi?sig="+regex1

r  = requests.get(url1)

data = r.text

soup = str(BeautifulSoup(data))

#print("\n*********************\n\nHere are the Prosite search results based on your regular expression:\n*********************\n\n")
#print(soup)
#print("\n\n\nNow, we will scrape the results for the top 5 gene results, while ignoring isoforms.\n\n")

# Importing the regular expression library and asking it to find all gene name formatted matches in the Prosite content,
# while ignoring isoforms, so that we don't have duplicates

import re

#souplist = re.findall(r"\|[a-zA-Z0-9]*?[\-]*?[a-zA-Z0-9]*?[\-|\|]", soup)

souplist = re.findall(r"\|[a-zA-Z0-9]*?\|", soup)

# Delete the last two entries which are "||" from the HTML of that same webpage.
    
del souplist[-1]
del souplist[-1]

# Strip out | and - which were initially kept as part of the regular expression to isolate gene names

striplist = ([s.replace('|', '') for s in souplist]) # remove the | from the string borders
striplist = ([s.replace('-', '') for s in striplist])

print("\n\n\n")

print("\n\nUSER 1: Here is the list of genes matched by your submitted ProSite pattern, ignoring isoforms. \nWe will be using only the first 5 best matches to construct your phylogenetic tree.\n\n")
for gene in striplist:
    print(gene)
    
print("\n\n\n")

# Assign a variable to the first 5 results in the list of resulting genes
    
User1Seq1 = striplist[0]
User1Seq2 = striplist[1]
User1Seq3 = striplist[2]
User1Seq4 = striplist[3]
User1Seq5 = striplist[4]

# Concatenate the User1 sequences into the uniprot.org FASTA formatted link, and open it in a new window,
# to demonstrate the FASTA formatted sequences
    
fastalink = ('https://www.uniprot.org/uniprot/?query='+User1Seq1+'%20OR%20'+User1Seq2+'%20OR%20'+User1Seq3+'%20OR%20%20'+User1Seq4+'%20OR%20%20'+User1Seq5+'&format=fasta&limit=5&sort=score')

import webbrowser

webbrowser.open_new(fastalink)

# NEXT STEP: Write the content of the above link to a txt FASTA file
# Using Beautiful Soup to do this!

r1  = requests.get(fastalink)

data1 = r1.text

user1soup = str(BeautifulSoup(data1))

user1soup = re.sub('<html><head></head><body>&gt;', '', user1soup)
user1soup = re.sub('</body></html>', '', user1soup)

print("\n\nHere are your top 5 matched sequences in FASTA format, USER 1:\n")
print(user1soup)

    
print("\nNow we will use this FASTA sequence to generate a phylogenetic tree\n\n")


text_file = open("User1FASTA.fsa", "w")
n = text_file.write(user1soup)
text_file.close()

quit()
