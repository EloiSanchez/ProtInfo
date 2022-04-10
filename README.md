# ProtInfo

This applet was made by Eloi Sanchez as a web scraping learning project, which can be [run in this link](https://share.streamlit.io/eloisanchez/protinfo/ProtInfo.py).

It looks for the protein given by the user on the Uniprot database and obtains, for now, only the sequence of the protein. The sequence is used to plot a chart with the percentages of the appearing aminoacids.

**Summary of techniques used/learned:**

- Web Scraping using the `requests` module to find information of the protein.
- Usage of the `streamlit` platform (https://docs.streamlit.io/) to create the frontend.
- Simple statistics and data visualisation with `matplotlib`, `regex` and `pandas`.

**Run locally**

Make sure that that you have installed the requirements listed in the `requirements.txt` file. You can run `pip install -r requirements.txt`. Clone the repository and run with `streamlit run ProtInfo.py`.

**About/Contact**

The only objective of this little project was to learn webscraping and the `streamlit` platform to create "apps". If you have any ideas that can be added to the project or simply want to contact with me you can do it following the links below:
- [E-mail](mailto:eloisanchez16@gmail.com)
- [GitHub](https://github.com/EloiSanchez)
- [LinkedIn](https://www.linkedin.com/in/eloi-sanchez-69094a21b/)
