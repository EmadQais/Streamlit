import streamlit as st
import pandas as pd
import numpy as np
#from IPython.core.interactiveshell import InteractiveShell
#InteractiveShell.ast_node_interactivity = "all"
import json,logging
import scrapy
from scrapy.crawler import CrawlerProcess

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
