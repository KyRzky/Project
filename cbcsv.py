import pandas as pd
import streamlit as st

sheet_id = "1I8yfLFfTQNscutI8kwY_bhrFCYNQxtWDJrLln9wdz0E"
sheet_name = "Data"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

df = pd.read_csv(url)

st.write(df)

# Remove the 'Bulan' column from the DataFrame as it will be used as the index
df.set_index('Bulan', inplace=True)

# Plot the line chart
st.bar_chart(df)