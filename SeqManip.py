"""
*** Sequence Manipulation Exercise ***
- Create a new Python script (text file)
- At the beginning of the script, define a DNA sequence (taken from 
https://github.com/jembrown/CompPhylo_Spr2015/blob/master/CodingSeq.txt)
- Print the length of the sequence to the screen along with text explaining 
the value
- Create and store the RNA equivalent of the sequence, then print to screen.
- Create and store the reverse complement of your sequence, then print to 
screen.
- Extract the bases corresponding to the 13rd and 14th codons from the 
sequence, then print them to the screen.
- Create a function to translate the nucleotide sequence to amino acids 
using the vertebrate mitochondrial genetic code (available from 
https://github.com/jembrown/CompPhylo_Spr2015/blob/master/VertMitTransTable.txt).
- Translate the sequence and print it to the screen.
- Be sure you've added comments to explain what this script is and what the 
different bits of code mean.
- Save this script as "seqManip.py" and commit it to your class GitHub repo.
"""

"""
BiopPython!!! woo. information from:
http://biopython.org/wiki/Seq
and
http://biopython.org/DIST/docs/tutorial/Tutorial.html#htoc17
and
http://biopython.org/DIST/docs/api/Bio.codonalign.codonseq.CodonSeq-class.html
"""

from Bio.Seq import Seq

from Bio.Alphabet import generic_dna, generic_rna

from Bio.codonalign import CodonSeq


dna="aaaagctatcgggcccataccccaaacatgttggttaaaccccttcctttgctaattaatccttacgctatctccatcattatctccagcttagccctgggaactattactaccctatcaagctaccattgaatgttagcctgaatcggccttgaaattaacactctagcaattattcctctaataactaaaacacctcaccctcgagcaattgaagccgcaactaaatacttcttaacacaagcagcagcatctgccttaattctatttgcaagcacaatgaatgcttgactactaggagaatgagccattaatacccacattagttatattccatctatcctcctctccatcgccctagcgataaaactgggaattgccccctttcacttctgacttcctgaagtcctacaaggattaaccttacaaaccgggttaatcttatcaacatgacaaaaaatcgccccaatagttttacttattcaactatcccaatctgtagaccttaatctaatattattcctcggcttactttctacagttattggcggatgaggaggtattaaccaaacccaaattcgtaaagtcctagcattttcatcaatcgcccacctaggc"

print "The length of the DNA seq is",len(dna),"basepairs"

#tell biopython that our string is DNA sequence
#generic_dna is from the Bio.Alphabet tells biopython what the string is it is, ie DNA, protiens etc
my_dna=Seq(dna,generic_dna)
#generic_dna tells biopython what the string is it is, ie DNA, protiens etc
#this is also useful because if you are working with multiple types of sequences, ie DNA, RNA, protien. biopython gives you error messages if you try and combine two types of strings that are specified as different things. ie RNA + DNA returns an error message. 
#if you forget what alphabet a sequence is using you can type:
#my_dna.alphabet

#.transcribe created RNA from DNA (just replacing t with u) 
my_rna=my_dna.transcribe()
print "The RNA sequence is",my_rna

#complement the DNA sequence
rcdna=my_dna.complement()
print "Reverse compliment of the DNA strand is",rcdna

#complement the RNA sequence
rcrna=my_rna.complement()
print "Reverse compliment of the RNA strand is",rcrna


#pull out specific codons.
#you need to feed CodonSeq a string, so we are taking the sequence object and making it a string
rcdna_str=str(rcdna)
#type(rcdna_str) #make sure it's a string not a Seq object
#print rcdna_str

#now make it into a codon seq object
codonseq=CodonSeq(rcdna_str)
#type(codonseq)
print codonseq
#slice and print the 13th and 14th condons
codon13= codonseq.get_codon(13)
print "The 13th codon is",codon13
codon14= codonseq.get_codon(14)
print "The 14th codon is",codon14


#mitochondria codon code
aas= "FFLLSSSSYY**CCWWLLLLPPPPHHQQRRRRIIMMTTTTNNKKSS**VVVVAAAADDEEGGGG"
base1= "TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG"
base2= "TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG"
base3= "TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG" 

#create a codon dictionary    
codondict = {}

for i in range(len(aas)):
    codondict[base1[i]+base2[i]+base3[i]]=aas[i]
#take the i letter from each base list, add them together, and then assign them to the same i in the amino acid sequence
#tests-
#print codondict
#codondict["TTT"]

#translate a sequence, you need to input the dictionary you want and the dna sequence
def translate(dna, codondict):
    codonseq=CodonSeq(dna) #turn this into a codon seq format
    codondict=codondict #assign variables
    numcodons= (len(codonseq))/3 #get number of codons
    translated_seq="" #start a string to add aas to
    for i in range(numcodons):
        translated_seq+=codondict[codonseq.get_codon(i)]
    print translated_seq
    

for i in range(numcodons):
    codondict[codonseq.get_codon(i)]
    

"""
how to do it more simply
"""

myString=dna
rna= myString.replace("t","u")
#replacing t with u.  To make sure you don't replace things weird, you can upper case the ones you have already replaced
print rna
