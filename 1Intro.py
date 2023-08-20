import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="My Online Therapist", page_icon=":tada:", layout="wide")




# ---- Title ----

st.subheader("Hello, I'm Zax :wave:")
st.title("Your Personal AI Mental Health Therapist")
st.write("In a world where the demands of modern life can often take a toll on our mental well-being. Meet me, Zax—an innovative AI robot meticulously crafted to serve as your personal mental health therapist.")

# ---- Purpose ----

st.write("---")
left_column, right_column = st.columns(2)
with left_column:
    st.header("My Job")
    st.write(
        """
        An AI mental health therapist, designed to provide support anytime you need it. With text-to-speech capabilities and our free app, I offers easily accessible and empathetic conversations, guiding you through challenges and offering coping strategies. Experience the convenience of therapeutic interactions on your terms, breaking down barriers to mental health care. I am here to lend an understanding ear and help you navigate your journey towards emotional well-being.
        """
    )
