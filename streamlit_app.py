
import streamlit as st
import pandas as pd



# Load the DataFrame
file_path = '/Users/alokeshirolkar/Library/CloudStorage/GoogleDrive-alokeshirolkar@gmail.com/My Drive/NEWAUSTRALIAN/streamlit/streamlitinput.csv'




def load_data():
    data = pd.read_csv(file_path)
    return data

def display_sidebar(df):
    st.sidebar.header("Settings")
    stock_options = df['Name of the Stock'].unique()
    selected_stock = st.sidebar.selectbox('Select a stock:', stock_options)
    return selected_stock

def show_stock_data(df, selected_stock):
    st.subheader(f"Stock Data for {selected_stock}")
    stock_data = df[df['Name of the Stock'] == selected_stock]
    st.dataframe(stock_data)

def show_recommendation(df, selected_stock):
    if selected_stock:
        recommendation = df[df['Name of the Stock'] == selected_stock]['Buy/Sell'].iloc[0]
        st.subheader(f"Recommendation for {selected_stock}")
        st.write(recommendation)

def app():
    st.set_page_config(layout="wide", page_title="Stock Buy/Sell Recommendations")
    st.title('Stock Buy/Sell Recommendations')
    df = load_data()
    st.header('Stock Performance Overview')
    selected_stock = display_sidebar(df)
    show_stock_data(df, selected_stock)
    show_recommendation(df, selected_stock)

if __name__ == "__main__":
    app()
