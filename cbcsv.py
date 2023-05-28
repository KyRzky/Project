import pandas as pd
import streamlit as st

sheet_id = "1I8yfLFfTQNscutI8kwY_bhrFCYNQxtWDJrLln9wdz0E"
sheet_name = "Data"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

df2020k2 = pd.read_csv(url)

st.write(df2020k2)

# Remove the 'Bulan' column from the DataFrame as it will be used as the index
df2020k2.set_index('Bulan', inplace=True)

# Plot the line chart
st.bar_chart(df2020k2)
