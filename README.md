# Entropy
Calculate the information entropy of the PE file

PEID software supports calculating the information entropy of PE files, and based on experiments, it is speculated that the software calculates the information entropy by
method may be:

1. H(x) = - sum i=1 to n p(i)*log2(p(i)) is the entropy calculation formula;
2. each section computes entropy independently, with the original size of each section (the size on disk) noted as x. Before computation, x is used to
Subtract the number of bytes at the end of the section that are zero;
3. two types of sections are not involved in the calculation (resource sections, sections with no data after removing the null byte);
4. calculate a weighted combination of the entropy of each section, with the weights taken from the (effective) length of each section.

Please write a PE file entropy calculation programme (software) based on the above idea.