# Import the libraries and set up the local environment
import streamlit as st
from dotenv import load_dotenv
load_dotenv()
import google.generativeai as genai
from pdf import read_pdf
from analysis import profile


#lets create the front end
st.header('📝 Resume Analysis: :red[Your LLM-Powered Resume Analyzer]👨🏼‍💻',
          divider='green')
st.subheader('👉Tips for using the application')
notes = f'''
* **Upload the Resume(PDF):** The first step is to upload the resume for analysis.
* **Paste the Target JD:** Share the details of the Job Description in the text area below.
* **Unleash the Power of LLMs:** Here, the Gemini Model will analyze the Job description supplied with the 
resume uploaded and will provide insights such as **ATS Score**, **Probability of getting selected** and so on.
'''
st.markdown(notes)

#sidebar
st.sidebar.header('📋Upload the Resume')
user_profile = st.sidebar.file_uploader('Please Upload the Resume here', type = ['pdf'])
st.sidebar.markdown('Created by Pooja H S Reddy')
st.sidebar.markdown('↪️Linkedin: www.linkedin.com/in/pooja-h-s-reddy-7696031b2')

#Job description box
st.subheader('Enter the Job Description', divider = True)
jd = st.text_area(label='Copy Paste the Job Description from Linkedin or any Job Portal',
                        max_chars=10000)

submit = st.button('🎯Get AI powered Insights')
if submit:
    st.markdown(profile(user_profile = user_profile, job_desc = jd))