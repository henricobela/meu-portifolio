import streamlit as st

def default_set_page_config():
    custom_html = """
    <div class="banner">
        <img src="https://img.freepik.com/premium-photo/wide-banner-with-many-random-square-hexagons-charcoal-dark-black-color_105589-1820.jpg" alt="Banner Image">
    </div>
    <style>
        .banner {
            width: 160%;
            height: 200px;
            overflow: hidden;
        }
        .banner img {
            width: 100%;
            object-fit: cover;
        }
    </style>
    """
    # Display the custom HTML
    st.components.v1.html(custom_html)
    st.set_page_config(
        initial_sidebar_state = "collapsed",
        page_icon = "utils/imgs/logotipo.jpg",
        page_title = "Portfolio", layout = "wide")