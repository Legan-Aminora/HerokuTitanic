import pandas as pd
import streamlit as st
import plotly.express as px

st.title("Titanic Clases")
st.header("Data Table")
st.markdown("**Titanic**")

@st.cache
def get_data():
    URL = "https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv"
    return pd.read_csv(URL)

df=get_data()
st.dataframe(df.head())

st.code("""@st.cache
def get_data():
    URL = "https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv"
    return pd.read_csv(URL)""", language="python")

#Step 1 sort

st.subheader("1)  Sorting in tables")
st.text("Top five most Rich People Aboard")
st.write(df.query("Fare>=263").sort_values("Fare", ascending=False).head())


#Step 2 - column filter
st.subheader("2)  Select a Column to see")
default_cols = ["Name", "Sex", "Parents/Children Aboard"]
cols = st.multiselect("Columns", df.columns.tolist(), default=default_cols)
st.dataframe(df[cols].head(10))

#Step 3 - Distributions - Sidebars
st.subheader("3)  Select a range for Fare with the sidebar") 
values = st.sidebar.slider("Fare Range", float(df.Fare.min()), float(df.Fare.clip(upper=513.).max()), (10., 500.)) 
hist = px.histogram(df.query(f"Fare.between{values}", engine='python' ), x="Fare", nbins=10, title="Price Distribution")
hist.update_xaxes(title="Fare") 
hist.update_yaxes(title=" Name") 
st.plotly_chart(hist)

#Step 4 - Another Sidebar

st.subheader("4)  Select a range for Fare with the sidebar") 
values2 = st.sidebar.slider("Ages", float(df.Age.min()), float(df.Age.clip().max()), (0., 90.)) 
hist2 = px.histogram(df.query(f"Age.between{values2}", engine='python' ), x="Age", nbins=40, title="Ages")
hist2.update_xaxes(title="Ages") 
hist2.update_yaxes(title=" How many people had that age ") 
st.plotly_chart(hist2)

#Step 5 - Radio buttons
name = df["Name"].str.split(".", expand=True)
name.columns = ["Title","Name2","drop"]
df = pd.concat([df,name], axis=1)
st.subheader("5)  Titles aboard")
Title = st.radio("Titles aboard:", df.Title.unique())
@st.cache
def get_info(Title):
    return df.query("Title==@Title")

dx = get_info(Title)
st.dataframe(dx[["Name","Sex","Age"]])



