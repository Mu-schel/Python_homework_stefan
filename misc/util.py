"""
Dictionary to translate DNA to Protein.
"""
codon_dict = {
    'UUU': 'F',      'CUU': 'L',      'AUU': 'I',      'GUU': 'V',
    'UUC': 'F',      'CUC': 'L',      'AUC': 'I',      'GUC': 'V',
    'UUA': 'L',      'CUA': 'L',      'AUA': 'I',      'GUA': 'V',
    'UUG': 'L',      'CUG': 'L',      'AUG': 'M',      'GUG': 'V',
    'UCU': 'S',      'CCU': 'P',      'ACU': 'T',      'GCU': 'A',
    'UCC': 'S',      'CCC': 'P',      'ACC': 'T',      'GCC': 'A',
    'UCA': 'S',      'CCA': 'P',      'ACA': 'T',      'GCA': 'A',
    'UCG': 'S',      'CCG': 'P',      'ACG': 'T',      'GCG': 'A',
    'UAU': 'Y',      'CAU': 'H',      'AAU': 'N',      'GAU': 'D',
    'UAC': 'Y',      'CAC': 'H',      'AAC': 'N',      'GAC': 'D',
    'UAA': 'Stop',   'CAA': 'Q',      'AAA': 'K',      'GAA': 'E',
    'UAG': 'Stop',   'CAG': 'Q',      'AAG': 'K',      'GAG': 'E',
    'UGU': 'C',      'CGU': 'R',      'AGU': 'S',      'GGU': 'G',
    'UGC': 'C',      'CGC': 'R',      'AGC': 'S',      'GGC': 'G',
    'UGA': 'Stop',   'CGA': 'R',      'AGA': 'R',      'GGA': 'G',
    'UGG': 'W',      'CGG': 'R',      'AGG': 'R',      'GGG': 'G'
}

"""
This is a function to read text files 
into a list of lines, removing the 
newline charachter at the end.
"""
# simple way to open files and remove newline charachters 
def read_file_into_lines(file_path):
    lines =  []
    with open(file_path,'r') as infile:
        for line in infile.readlines():
            cleaned = line.rstrip() #just get rid of new line characters 
            lines.append(cleaned)
    return lines

"""
A function to parse through a fasta file
and return a dictionary with the ID and 
the nucleotide sequence as items.
"""
def parse_fasta(lines_list):
    current_sequence = ''
    current_id = ''
    sequences = {}

    for line in lines_list:
        # if line.startswith('>'):
        if line[0] == '>':
            sequences[current_id] = current_sequence
            current_id = line[1:]
            current_sequence = ''
        else:
            current_sequence = current_sequence + line

    sequences[current_id] = current_sequence
    del sequences['']
    return sequences















