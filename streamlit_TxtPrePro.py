import streamlit as st
import pandas as pd
import numpy as np
# import plotly.express as px
# import time
# from keras.preprocessing.text import text_to_word_sequence
from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import random
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re

#text
st.title("My first App")
st.header("My first header")
st.subheader("My first sub header")

#datafram
df = pd.DataFrame(data = np.random.rand(100, 3), columns=["A", "B", "C"])
st.table(df.head())

#Plots
#fig = px.scatter(df, x = "A", y = "B")
#st.write(fig)
#st.line_chart(df)

# Scraping the text from websites and save the text to the local text

lineCount = 0
paragraphsCount = []
paragraphs = []
listCount = []
with open(r'Links.txt','r') as txt:
    for line in txt:
        page = requests.get(line.strip())
        soup = BeautifulSoup(page.content, 'html.parser') # Extract contect
#         print(f'Number of paragraphs is :  {len(soup.find_all("p"))}')
        paragraphsCount.append(len(soup.find_all("p")))
        lineCount += 1
        listCount.append(lineCount)
        FileName = str(lineCount)
        FileName = 'TextPreprocessing\\Text\\'+FileName+'.txt'
        f = open(FileName,'w',encoding = 'utf-8')
        for i in range(len(soup.find_all('p'))) : 
            text = soup.find_all('p')[i].get_text() 
            paragraphs.append(text)
            f.write(soup.find_all('p')[i].get_text())
            f.write('\n')
        f.close()
        
st.write(lineCount)

dataFrame = pd.DataFrame(paragraphs)
st.write(dataFrame)