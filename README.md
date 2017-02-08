# bioinformatics-scripts
A collection of code snippets and scripts related to my bioinformatics works

## Working with fasta files
* fasta_split_size.py

Python script to split a multi-sequence fasta file into smaller ones with similar sub-total sizes. For example, this can be used to split 1 Mb fasta file containing 100 sequences into smaller ones of size around 1 Kb. The resulting fasta files will have similar sub-total size of 1 Kb and may contain different number of sequences.
Modified from [this script](https://github.com/enormandeau/Scripts/blob/master/fasta_split.py)

* splitFasta.pl

Perl script to split a fasta file into chunks of certain size or number of sequence.
