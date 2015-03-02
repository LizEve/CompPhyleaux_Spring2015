# -*- coding: utf-8 -*-
"""
Created on Mon Feb 23 15:47:46 2015

@author: ChatNoir
"""

"""
An object is an instance of a class. A class doesn't create objects, 
but it created a blueprint for making objects.
"""

#example from book
class DNARecord(object):
#these are defaults for the attributes of the class
    sequence = 'ACGTAGCTGACGATC'
    gene_name = 'ABC1'
    species_name = 'Drosophila melanogaster'
#self refers to the object you are creating. so self.sequence refers to whichever 
#sequence corresponds to the current instance of that class you are calling
    def complement(self):
        replacement1 = self.sequence.replace('A', 't')
        replacement2 = replacement1.replace('T', 'a')
        replacement3 = replacement2.replace('C', 'g')
        replacement4 = replacement3.replace('G', 'c')
        return replacement4.upper()       
        
    def get_AT(self):
        length = len(self.sequence)
        a_count = self.sequence.count('A')
        t_count = self.sequence.count('T')
        at_content = (a_count + t_count) / length
        return at_content
    def get_fasta(self):
        safe_species_name = self.species_name.replace(' ','_')
        header = '>' + self.gene_name + '_' + safe_species_name
        return header + '\n' + self.sequence + '\n'


d1 = DNARecord()
d1.sequence = 'ATATATTATTATATTATA'
d1.gene_name = 'COX1'
d1.species_name = 'Homo sapiens'

d2 = DNARecord()
d2.sequence = 'CGGCGGCGCGGCGCGGCG'
d2.gene_name = 'ATP6'
d2.species_name = 'Gorilla gorilla'
for r in [d1, d2]:
    print('Created ' + r.gene_name + ' from ' + r.species_name)
    print('AT is ' + str(r.get_AT()))
    print('complement is ' + r.complement())
    
"""
Created COX1 from Homo sapiens
AT is 1
complement is TATATAATAATATAATAT
Created ATP6 from Gorilla gorilla
AT is 0
complement is GCCGCCGCGCCGCGCCGC
"""
"""
but this is setting each variable seperately, we want to do it all at once
and make sure that it happens every time before trying to use the objects
"""

class DNARecord(object):
#init is a built in function (a constructor) that lets you assign a bunch of information to each instance of the class
#
    def __init__(self, sequence, gene_name, species_name):
        self.sequence = sequence
        self.gene_name = gene_name
        self.species_name = species_name
        
    def complement(self):
        ...
        
    def get_AT(self):
        ...

d1 = DNARecord('ATATATTATTATATTATA', 'COX1', 'Homo sapiens')
print(d1.complement())

"""
Bass Class

pretend we have another class about protiens, this class has a shared function and the same input
so we put the shared functions and the identicle input into a base class
then both the dna and prot classes inherit this base class as follows
the benefit is only having to define useful fuctions once
"""

class SequenceRecord(object):
    def __init__(self, sequence, gene_name, species_name):
        self.sequence = sequence
        self.gene_name = gene_name
        self.species_name = species_name
    def get_fasta(self):
        safe_species_name = self.species_name.replace(' ','_')
        header = '>' + self.gene_name + '_' + safe_species_name
        return header + '\n' + self.sequence + '\n'

#now we pass dna the base class name, and only list the funcitons unique to dna class
class DNARecord(SequenceRecord):
    
    def complement(self):
        ...
        
    def get_AT(self):
        ...
        
#you can override anything from the superclass by just re-defining in the subclass
        
"""
reg ex to check if species name looks like sp name
capital letter, followed by many lowercase, a space, then a string of lower
"""

import re
class SequenceRecord(object):
    def __init__(self, sequence, gene_name, species_name):
       if not re.match(r'[A-Z][a-z]+ [a-z]+', species_name):
           exit(species_name + ' is not a valid species name!')
        self.sequence = sequence
        self.gene_name = gene_name
        self.species_name = species_name