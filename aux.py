# Some auxiliary variables for the code

# List of colors for plots
colors = ['#2bad79', '#2b5fad', '#ad2b5f', '#ad792b', '#b7ae2d']

# Dictonaries for conversion between different aminoacid nomenclatures
AMapThreeToOne = {'CYS': 'C', 'ASP': 'D', 'SER': 'S', 'GLN': 'Q', 'LYS': 'K',
     'ILE': 'I', 'PRO': 'P', 'THR': 'T', 'PHE': 'F', 'ASN': 'N', 
     'GLY': 'G', 'HIS': 'H', 'LEU': 'L', 'ARG': 'R', 'TRP': 'W', 
     'ALA': 'A', 'VAL':'V', 'GLU': 'E', 'TYR': 'Y', 'MET': 'M'}

AMapOneToThree = {}
for key in AMapThreeToOne.keys():
    AMapOneToThree[AMapThreeToOne[key]] = key