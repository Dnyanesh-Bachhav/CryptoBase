import streamlit as st
from streamlit_option_menu import option_menu
import contactus
import About_us
import home
import live_pricing
base = "dark"

st.set_page_config(
    # page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state='auto'
    # initial_sidebar_state="expanded",
    # menu_items={
    #     'Get Help': 'https://www.extremelycoolapp.com/help',
    #    'Report a bug': "https://www.extremelycoolapp.com/bug",
    #    'About': "# This is a header. This is an extremely cool app!"
    # }
)


# with st.sidebar:
# st.title('Home')
# st.subheader('Prediction')
#st.subheader('Live price')
# st.subheader('Comparison')
#st.subheader('Crypto Info')
#st.subheader('Contact Us')
selected = option_menu(


    menu_title=None,

    orientation="horizontal",

    options=["Home", "Live pricing", "Basic Info",
             "Trading tips", "Comparison", "About Us","Contact us"],
    default_index=0
)

if selected == "Home":
    #home.home()
    st.title("This is home page")
elif selected == "Live pricing":
    live_pricing.live_price()
    #st.title("This is live pricing section")
elif selected == "Basic Info":
    st.title("This is Basic Info page")
elif selected == "Trading tips":
    st.title("This is trading tips pAGE")
elif selected == "About Us":
     About_us.aus()
elif selected == "Comparison":
    st.title("This is comparison page")
elif selected == "Contact us":
    contactus.callus()
