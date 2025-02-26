from pdf import read_pdf
import os
import google.generativeai as genai
import streamlit as st

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
model = genai.GenerativeModel('gemini-1.5-pro') #Initiate the model

def profile(user_profile, job_desc):
    if user_profile is not None:
        pdf = read_pdf(user_profile)
        st.sidebar.markdown('The Resume has been Uploaded')
    else:
        st.warning('Upload the Resume')
    
    #ATS Score
    ats_score = model.generate_content(f''' Compare the resume{pdf} with
                                       job description {job_desc} and suggest
                                       the ATS Score(in percentage) of the resume''')
    
    #Chances of selection
    prob_score = model.generate_content(f''' Compare the resume{pdf} with
                                       job description {job_desc} and suggest
                                       the Probability(in percentage) of the getting selected''')
    
    #Keyword Analysis
    keyword = model.generate_content(f''' Analyse the Keywords missing in the resume{pdf} with
                                       job description {job_desc} and mention them in bold and
                                       give narratives how to add them in the resume''')
    
    #Tailored projects
    projects = model.generate_content(f''' Compare the resume{pdf} with
                                       job description {job_desc} and give me the list of projects/
                                       hackathons(in bold) with problem statement and 
                                       the Probability of the getting selected as per the Job description''')
    
    #Swot Analysis
    swot = model.generate_content(f''' Compare the resume{pdf} with
                                       job description {job_desc} and provide a 
                                       SWOT analysis''')
    
    #Improvement Tips
    Improvement = model.generate_content(f''' Suggest Improvements to the resume{pdf} after comparing with
                                       job description {job_desc} so that the ATS Score of the resume increases 
                                       and it is better aligned and mention the comments in bold''')
    
    #Creating the new Resume narrative..
    resume = model.generate_content(f''' Recreate the  new resume basis the {pdf} to highlight the relevent 
                                    skill, projects and experience according to the job description {job_desc}''')
    
    #Display the results
    return(st.write(ats_score.text),
           st.write(prob_score.text),
           st.write(keyword.text),
           st.write(projects.text),
           st.write(swot.text),
           st.write(Improvement.text),
           st.write(resume.text))

