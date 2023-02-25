import streamlit as st
from matplotlib import image
import os
import plotly.express as px
import pandas as pd


st.title("Dashboard - Titanic Data")

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "titanic.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "titanic.csv")

img = image.imread(IMAGE_PATH)
st.image(img)

df = pd.read_csv(DATA_PATH)
st.dataframe(df)

df = df.dropna()
df['Age_bucket'] = [int(val/10) for val in df['age'].values ] 

species = st.selectbox("Select the town:", df['embark_town'].unique())


fig_1 = px.histogram(df[df['embark_town'] == species], x="Age_bucket")
st.plotly_chart(fig_1, use_container_width=True)


df['not_survived'] = [1 if val==0 else 0 for val in df['survived'].values ] 

st.subheader('Number of survived based on Age rage')
st.bar_chart(df,x='Age_bucket',y=['survived','not_survived'])


st.subheader('Number of survived based on passenger class')
st.bar_chart(df,x='class',y=['survived','not_survived'])