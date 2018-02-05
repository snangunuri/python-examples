#!/usr/bin/python
import sys
input_file= sys.argv[1]
gene= sys.argv[2]
print 'argument is', gene
sequence=""
with open (input_file, 'r') as myfile:
  for line in myfile:
    if gene in line:
      for line in myfile:
        if line.startswith('>'):
          break
        else:
          sequence = sequence + line.strip()
print "printing string"
print("The sequence for %s is %s" % (gene, sequence))
