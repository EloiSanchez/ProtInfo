import streamlit as st
import functions as func

st.write("""
# Protein Finder

You can try with proteines such as Caseine, Collagen or Hemoglobin! 

Check the left side panel for more information.
        """)

userQuery = st.text_input('What protein are you looking for?')
if userQuery:
    proteinResults = func.FindProteins(userQuery)
    if not proteinResults.empty:
        st.write(proteinResults)
        
        leftColumnSelect, rightColumnSelect = st.columns([2,1])
        index = rightColumnSelect.selectbox('What protein do you want to analyse?', 
                                            options=['Index'] + list(range(len(proteinResults.index))))
        if type(index) == int:
            selectorText = f'Printing information for **{proteinResults.at[index, "Name"]}**'
            
            func.protInfo(proteinResults.at[index, 'Link'])
            st.write('More info at https://www.uniprot.org' + proteinResults.at[index, 'Link'])
            leftColumnSelect.write(selectorText)
    else:
        st.write('We didn\'t find anything... Try again!')

with st.sidebar:
    st.write('**What is this?**')
    st.write('This applet was made by Eloi Sanchez as a web scraping learning',
             'project.')
    st.write('It looks for the protein given by the user on the Uniprot database and ',
             'obtains, for now, only the sequence of the protein. The sequence is used',
             'to plot a chart with the percentages of the appearing aminoacids.')
    st.write('**Summary of techniques used/learned:**')
    st.write("""
            - Web Scraping using the `requests` module to find information of the protein.
            - Usage of the `streamlit` platform (https://docs.streamlit.io/) to create the frontend.
            - Simple statistics and data visualisation with `matplotlib`, `regex` and `pandas`.
             """)
    st.write('**About/Contact**')
    st.write('The only objective of this little project was to learn webscraping and',
             'the `streamlit` platform to create "apps". If you have any ideas to',
             'or simply want to contact with me you can do it following the links below:')
    st.write("""
             - [E-mail](mailto:eloisanchez16@gmail.com)
             - [GitHub](https://github.com/EloiSanchez)
             - [LinkedIn](https://www.linkedin.com/in/eloi-sanchez-69094a21b/)
             """)
    