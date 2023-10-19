from dotenv import load_dotenv
import os
import streamlit as st
import pandas as pd
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI
import matplotlib

matplotlib.use('TkAgg')
st.set_page_config(layout="wide")

load_dotenv()
API_KEY = os.environ['OPENAI_API_KEY']


llm = OpenAI(api_token =API_KEY)
pandas_ai = PandasAI(llm)


st.title("Data Analysis using PandasAI")
uploaded_file = st.file_uploader("Upload a CSV file for Analysis", type=['csv'])


if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    c = st.container()
    c.write(df)

    prompt = st.text_area("Enter your promt:")

    if st.button("Generate"):
        if prompt:
            with st.spinner("Generating response...."):
                st.write(pandas_ai.run(df,prompt=prompt))
        else:
            st.warning("Please enter a prompt")
