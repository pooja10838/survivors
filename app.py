from vega_datasets import data
import streamlit as st
import altair as alt
import pandas as pd
from PIL import Image
def main():
    df = load_data()
    ep_data = load_ep_data()

    page = st.sidebar.selectbox("Choose a page", ["Homepage", "Sociodemographic", "Exploration"])
    image = Image.open("images/image.png")

    if page == "Homepage":
        st.header("Covid-19 Recovered Data")
        st.write("Please select a page on the left.")
        st.write(df)

    elif page == "Sociodemographic":
        st.title("Epidemiological")
        st.write(ep_data)

    elif page == "Exploration":
        st.title("Data Exploration")
        st.image(image, width =100)
        x_axis = st.selectbox("Choose a variable for the x-axis", df.columns, index=3)
        y_axis = st.selectbox("Choose a variable for the y-axis", df.columns, index=4)
        visualize_data(df, x_axis, y_axis)

@st.cache
def load_data():
    df = data.cars()
    return df
def load_ep_data():
    ep_data = pd.read_csv("data/epidemiological.csv")
    return ep_data

def visualize_data(df, x_axis, y_axis):
    graph = alt.Chart(df).mark_circle(size=60).encode(
        x=x_axis,
        y=y_axis,
        color='Origin',
        tooltip=['Name', 'Origin', 'Horsepower', 'Miles_per_Gallon']
    ).interactive()

    st.write(graph)

if __name__ == "__main__":
    main()

