#!/usr/bin/env python
"""
A utility script to split a large FASTA file into smaller ones,
with similar arbitrary sizes (total bp) in each one. 

Takes two arguments:
    1) The large FASTA file that needs to be split
    2) The approximate total size (bp) of sequences that should be put into each FASTA
"""
#   define a usage message
usage = """Split_FASTA.py - splits a large FASTA file into similar sub-total sizes.

Usage:
Split_FASTA.py [FILE] [SUB-TOTAL SIZE]

Splits [FILE] into a collection of smaller files, with [SUB-TOTAL SIZE] bp
in each one."""

#   To take arguments on the command line
import sys
#   To do some math
import math
#   To read/write FASTA. Wrap in a try/except
try:
    from Bio import SeqIO
except ImportError:
    print "This script requires BioPython to be installed!"

#   Simple check to make sure that the correct number of arguments are given
if len(sys.argv) != 3:
    print usage
    exit(1)

#   Set these names so that it is easier to follow them in the code
to_split = sys.argv[1]
num_seqs = sys.argv[2]

#   Make sure that the file provided is readable. 
try:
    open(to_split, 'r')
except IOError:
    print "Error! " + to_split + " does not exist, or is not readable!"
    exit(1)

#   And make sure that the second argument is a positive integer
#   The try-Except block tests for integer, and the if tests for positive
try:
    int(num_seqs)
except ValueError:
    print "Error! Please provide a positive integer!"
    exit(1)
if int(num_seqs) <= 0:
    print "Error! Please provide a positive integer!"
    exit(1)

#   Read in the FASTA file
all_fasta = SeqIO.parse(to_split, 'fasta')
#   How many files to split into?
#num_files = int(math.ceil(len(all_fasta)/float(num_seqs)))
#   Print a little message
print "Will split " + to_split + " into  files, with maximum " + str(num_seqs) + " bp per file."
#   Start splitting!
i = 0
l = 0
curlen = 0
totallen = 0
sub_fasta = []
sub_fasta_rec = []

for record in all_fasta:
    if (curlen < int(num_seqs)):
        curlen += len(record.seq)
    #   Generate the filename
    #   strip off the extension, and get the rest
#        filename = to_split.split('.')[:-1][0] + '_' + str(l) + '.fasta'
    #   Write the sequences into the file
    #    SeqIO.write(all_fasta[l], filename, 'fasta')
    #   increment the counter
#        sub_fasta_rec.append(record)
        sub_fasta_rec.append(record)
    else:
	sub_fasta.append(sub_fasta_rec)
	sub_fasta_rec = []
        sub_fasta_rec.append(record)
        curlen = len(record.seq)
    l += 1
    totallen += len(record.seq)
sub_fasta.append(sub_fasta_rec)
print "Total original records: ",l,", with ",totallen," bases."

l = 0
curlen = 0
currec = 0
totallen = 0
totalrec = 0
for fasta in sub_fasta:
#    print len(fasta)
    filename = to_split.split('.')[:-1][0] + '_' + str(l) + '.fasta'
    SeqIO.write(fasta, filename, "fasta")
    for rec in fasta:
	curlen += len(rec.seq)
	currec += 1
	totallen += len(rec.seq)
	totalrec += 1
    print "Written ",currec," records (",curlen," bp) to ",filename
    curlen = 0
    currec = 0
    l += 1
print "Total records: ",totalrec,". Total bases: ",totallen,"."

