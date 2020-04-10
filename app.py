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
        st.header("Epidemiological Data")
        st.write( ep_data.drop(['userId'], axis=1))
        st.header("Epidemiological Charts")
        st.subheader("Bar Plots")
        x_axis = st.selectbox("Choose a variable for the x-axis", ep_data.columns, index=3)
        visualize_descriptive(ep_data, x_axis)
        
        if  ep_data['age'] < 18:
            ep_data['ageRange'] = '<18'
        elif ep_data['age'] >= 18 and ep_data['age'] <= 24:
            ep_data['ageRange'] = '18-24'
        elif ep_data['age'] >= 25 and ep_data['age'] <= 34:
            ep_data['ageRange'] = '25-34'
        elif ep_data['age'] >= 35 and ep_data['age'] <= 44:
            ep_data['ageRange'] = '35-44'
        elif ep_data['age'] >= 45 and ep_data['age'] <= 54:
            ep_data['ageRange'] = '45-54'
        elif ep_data['age'] >= 55 and ep_data['age'] <= 64:
            ep_data['ageRange'] = '55-64'
        elif ep_data['age'] >= 65:
            ep_data['ageRange'] = '>65'
        else :
            ep_data['ageRange'] = 'Unknown'
         
        
            
        ep_data['age'].value_counts().plot(kind='bar', figsize=(7, 6), rot=0)
        plt.xlabel("Gender", labelpad=14)
        plt.ylabel("Count of People", labelpad=14)
        plt.title("Count of People Who Received Tips by Gender", y=1.02)
        st.pyplot()
        
        
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

