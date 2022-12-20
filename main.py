import streamlit as st
import pandas
from ast import literal_eval

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)
with col1:
    st.image("images/photo.JPG")
with col2:
    st.title("Ethan (Shihui) Liu")
    content = """
        Hi, I am Ethan (Shihui) Liu. I graduated in 2022 with a Master of Science in Computing from the Cardiff 
    University in the UK with a focus on using Python.
        """
    st.info(content)

content2 = """
下面是所买物品的清单
"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])
df = pandas.read_csv("data.csv")
with pandas.option_context("display.max_colwidth", None):
    print(type(df["Urls"][2:3]))
# print(df)
# df["images"] = df["images"].str.split(",")
# df["urls"] = df["urls"].str.split(",")
# print(df.to_string())
# df.to_csv("data.csv")

with col3:
    for index, row in df[:3].iterrows():
        st.header(row["Title"])
        st.write(row["Description"])
        for image in row["Images"].split(", "):
            st.image("images/" + image)
        for url in row["Urls"].split(", "):
            st.write(f"[Source Page]({url})")
        st.write(row["Purchase price"])
        st.write(row["Promotional activity"])