import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import streamlit.components.v1 as component


from htbuilder import HtmlElement, div, br, hr, a, p, img, styles
from htbuilder.units import percent, px


def image(src_as_string, **style):
    return img(src=src_as_string, style=styles(**style))


def link(link, text, **style):
    return a(_href=link, _target="_blank", style=styles(**style))(text)


def layout(*args):

    style = """
    <style>
     .stApp { bottom: 150px; }
    </style>
    """

    style_div = styles(
        position="fixed",
        left=0,
        bottom=0,
        margin=px(0, 0, 0, 0),
        width=percent(100),
        color="black",
        text_align="center",
        height="auto",
        opacity=1
    )

    style_hr = styles(
        display="block",
        margin=px(8, 8, "auto", "auto"),
        border_style="inset",
        border_width=px(2)
    )

    body = p()
    foot = div(
        style=style_div
    )(
        hr(
            style=style_hr
        ),
        body
    )

    st.markdown(style, unsafe_allow_html=True)

    for arg in args:
        if isinstance(arg, str):
            body(arg)

        elif isinstance(arg, HtmlElement):
            body(arg)

    st.markdown(str(foot), unsafe_allow_html=True)


def footer():
    myargs = [
        image('https://upload.wikimedia.org/wikipedia/commons/thumb/e/eb/Coat_of_arms_of_Jakarta.svg/220px-Coat_of_arms_of_Jakarta.svg.png',
              width=px(50), height=px(50)),
        br(),
        link("https://twitter.com/ChristianKlose3", "Home"),
        "-||-",
        link("https://twitter.com/ChristianKlose3", "Jelajah"),
        "-||-",
        link("https://twitter.com/ChristianKlose3", "Tentang Jakarta"),
        br(),
        link("https://twitter.com/ChristianKlose3", "Informasi Covid-19"),
        "-||-",
        link("https://twitter.com/ChristianKlose3", "Profil Pemerintahan"),
        "-||-",
        link("https://twitter.com/ChristianKlose3", "Informasi Penduduk"),
    ]
    layout(*myargs)
    


if __name__ == "__main__":
    footer()

# Create a container for the header
header_container = st.container()

# Add content to the header container
with header_container:
    col1, col2, col3 = st.columns([1, 3, 1])

    with col1:
        img = Image.open("D:\WebPhytonUAS\Monas.jpg")
        st.image(img)

    with col2:
        st.markdown("<h1 style='text-align: center; color:white;'>Website DKI Jakarta</h1>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align: center; color:white;'>Sukses Jakarta Untuk Indonesia</h4>", unsafe_allow_html=True)

    with col3:
        st.write(" ")


@st.cache(ttl=600)
def run_query(query):
    rows = conn.execute(query, headers=1)
    return rows



# Create a container for the main content
main_container = st.container()

# Add content to the main container
with main_container:
    st.write(' ')
    st.write(' ')

    st.markdown("<h1 style='text-align: center; color:white;'>Informasi Covid-19 DKI Jakarta</h1>", unsafe_allow_html=True)

    first_choice = st.selectbox("First level options", ["2020K2", "2020K3","2020K4", "2021K1", "2021K2", "2021K3", "2021K4", "2022K1", "2022K2", "2022K3", "2022K4", "2023K1"])

    if first_choice == '2020K2':
        sheet1_url = st.secrets["gsheets"]["Sheet1"]
        rows = run_query(f'SELECT * FROM "{sheet1_url}"')
        for row in rows:
            st.write(f"{row.Bulan} has a :{row.Positif}: :{row.Sembuh}: :{row.Meninggal}:")
    elif first_choice == '2020K3':
         sheet2_url = st.secrets["gsheets"]["Sheet2"]
         rows = run_query(f'SELECT * FROM "{sheet2_url}"')
         for row in rows:
            st.write(f"{row.Bulan} has a :{row.Positif}: :{row.Sembuh}: :{row.Meninggal}:")
