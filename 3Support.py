import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="My Online Therapist", page_icon=":tada:", layout="wide")



# ---- Title ----

st.title("Do You Feel You Need More Help?")
st.subheader("No worries! We totally understand below are various links to help navigate your mental health")

# ---- Help ----

st.write("---")
left_column, right_column = st.columns(2)
with left_column:
    st.header("Psychology Today's Therapist Finder")
    st.write("An online platform designed to help individuals find therapists and mental health professionals in their local area. It offers a comprehensive database of therapists, psychologists, counselors, and other mental health providers, allowing users to search for professionals who match their specific needs and preferences.")
    st.markdown("[Learn More](https://www.psychologytoday.com/ca/therapists)")

with right_column:
    st.header("Government of Canada's Suicide Prevention Website")
    st.write("Provides a range of resources and support to address mental health challenges and reduce suicide rates. It offers helpline information for immediate assistance, educational materials to understand signs of suicidal thoughts, and strategies to help at-risk individuals. The website showcases prevention initiatives, research data, and culturally sensitive resources, including support for Indigenous communities.")
    st.markdown("[Learn More](https://www.canada.ca/en/public-health/services/suicide-prevention/warning-signs.html)")
# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Us!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/YOUR@MAIL.COM" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.markdown("""
                 Contact Us


                 +1 (416)-731-4937



                                                syed.islam42123@gmail.com
                   """)        
