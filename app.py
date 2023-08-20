import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Online Therapist", page_icon=":tada:", layout="wide")
def load_lottieurl(url):
  r = requests.get(url)
  if r.status_code != 200:
    return None
  return r.json()

# ---- URL ----
lottie_coding = load_lottiefile("lottiefiles/Mental.json")
lottie_coding = load_lottieurl("https://app.lottiefiles.com/animation/5486dc8a-f235-40e9-a525-84371b768ff1")

# ---- Title ----
with st.container():
  st.subheader("Hello, I'm Zax :wave:")
  st.title("Your Personal AI Mental Health Therapist")
  st.write("In a world where the demands of modern life can often take a toll on our mental well-being. Meet me, Zax—an innovative AI robot meticulously crafted to serve as your personal mental health therapist.")
  
# ---- Purpose ----
with st.container():
  st.write("---")
  left_column, right_column = st.columns(2)
  with left_column:
    st.header("My Job")
    st.write(
      """
      An AI mental health therapist, designed to provide support anytime you need it. With text-to-speech capabilities and our free app, Zax offers easily accessible and empathetic conversations, guiding you through challenges and offering coping strategies. Experience the convenience of therapeutic interactions on your terms, breaking down barriers to mental health care. Zax is here to lend an understanding ear and help you navigate your journey towards emotional well-being.
      """
    )
  with right_column:
    st_lottie(lottie_coding, height=300, key="coding")
