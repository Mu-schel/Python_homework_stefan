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