import streamlit as st
import requests
import collections
from bs4 import BeautifulSoup
import pandas as pd
import re
import matplotlib.pyplot as plt
import aux

def FindProteins(name):
    # Get results from Uniprot and read them as HTML
    r = requests.get('https://www.uniprot.org/uniprot/?query=' + name + '&sort=score')
    parsedHtml = BeautifulSoup(r.text, 'html.parser')
    
    # Get the results from the page and find the data of interest
    protNames, links, uniprotIds, organisms = [], [], [], []
    entries = parsedHtml.find_all("tr", attrs={'class':'entry'})
    for entry in entries:
        protNames.append(entry.find('div', attrs={'class':'short'}).text)  # Protein name
        link_header = entry.find('td', attrs={'class':'entryID'})
        link = str(link_header).split('"')                                 # Link to the protein in uniprot
        links.append(link[-2])
        uniprotIds.append(link[-1][1:7])                                   # Uniprot ID
        organisms.append(entry.find('td', attrs={'class':'number'}).findPrevious().text)  # Organism
    return pd.DataFrame({'Name':protNames, 'Organism':organisms, 'Uniprot ID':uniprotIds, 'Link':links})

def protInfo(url):
    r = requests.get('https://www.uniprot.org' + url)
    parsedHtml = BeautifulSoup(r.text, 'html.parser')
    sequence = [s for s in parsedHtml.find('pre', attrs={'class':'sequence'}).text.split() if s[-1] not in '0123456789']
    # Some sequences are appended a digit at the beginning and must be removed
    pattern = re.compile(r'\D')
    for i in range(len(sequence)):
        # This feels unnecessarily complicated
        if sequence[i][0] in '0123456789':
            sequence[i] = "".join(pattern.findall(sequence[i]))
    sequence = "".join(sequence)
    count = collections.Counter(sequence)
    # Transform the names of the AAs
    auxDict = {}
    for key in count:
        auxDict[aux.AMapOneToThree[key]] = count[key]
    count = auxDict
    # Make a bar plot
    fig, ax = plt.subplots()
    bars = ax.bar(count.keys(), [float(s) for s in count.values()], color=aux.colors[0])
    ax.set_ylabel('% of aminoacid')
    plt.xticks(rotation=45)
    st.write('Percentages of the different amino acids of the sequence')
    st.pyplot(fig)