from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Resume.pdf"
profile_pic = current_dir / "assets" / "Profile picture.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Ashutosh Singh"
PAGE_ICON = ":wave:"
NAME = "Ashutosh Singh"
DESCRIPTION = """
I am an enthusiastic and dedicated engineering graduate, eager to
apply my academic knowledge and practical skills to contribute to your
company's success. With a strong foundation in Artificial Intelligence and
Data Science, I possess a keen problem-solving mindset and a passion
for innovation. During my studies, I demonstrated my ability to work
collaboratively in diverse teams, adapting to challenges and delivering
results. I am excited to join your team, bring fresh perspectives, and grow
as a professional while making meaningful contributions to your projects
"""
EMAIL = "ashusingh3414@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com/in/ashutoshsingh8900",
    "GitHub": "https://github.com/Ashu8900",
}
PROJECTS = {
    "🏆 MLOPS": "https://github.com/Ashu8900/ML_projects",
    "🏆 Spam Classification" : "https://github.com/Ashu8900/spam-classification",
    "🏆 Movie Recommendation" : "https://github.com/Ashu8900/Movie-Recommendation",
    "🏆 Kidney Stone Detection" : "https://drive.google.com/drive/folders/17LCPJm74MjFt0QZbPdM1STwxCwVaC__9?usp=drive_link",
    "🏆 Ipl Win Prediction" : "https://github.com/Ashu8900/IPL-WIN_PREDICTION",
    "🏆 Resume Parser": "https://github.com/Ashu8900/CodeClause_Building-a-Resume-Parser-Using-NLP-Spacy-and-Machine-Learning",
    "🏆 Telecom Churn Prediction ": "https://github.com/Ashu8900/CodeClause_Churn-Prediction-in-Telecom-Industry-using-Logistic-Regression",
    "🏆 Finalist of Kavach Cyber security Hackathon 2023" : "https://drive.google.com/file/d/1JoEcesm26-2G5hhbmePLaKEZU59N-PBD/view",
    "🏆 Intech Winner 2K22 ": "https://drive.google.com/file/d/1Q0rIk0eNA52BACyk_BTPQQ0XV4B7Rf8-/view",
    
    
}

CERTIFICATES = {
     "Training Completion Certificate by Coincent" : "https://drive.google.com/file/d/1_AniI9uirDmzKxJ5rZlCpwmGoWvO8jSb/view?usp=share_link",
    "Internship Completion Certificate" :" https://drive.google.com/file/d/1tIFil8RE2npUiH66nuF6R_SMZ6odqW81/view?usp=share_link",
    "Machine Learning Training Certificate" : "https://drive.google.com/file/d/1GnLZjU2xO9CkK6HIXDeeFPpoTDCkiwhF/view?usp=share_link",
    "AWS Cloud Foundation Course" : "https://drive.google.com/file/d/1feJh1LII8fyi8dNtH2_ItUWJ-knBZ5au/view?usp=share_link"
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 =  st.columns(2,gap="small")
col3, col4 =  st.columns(2,gap="small")
with st.container():
    with col1:
        st.image(profile_pic, width=250) 
    with col2:
        st.title(NAME)
        
with st.container():
        st.write(DESCRIPTION)

with st.container():
    with col3:
        st.download_button(
            label=" 📄 Download Resume",
            data=PDFbyte,
            file_name=resume_file.name,
            mime="application/octet-stream",
        )
    with col4:
        st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write("---")
st.write(
    """
- ✔️ Strong hands on experience and knowledge in Python and Excel
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write("---")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas), Artificial Intelligence, Machine Learning, Deep Learning, Natural Language Processing,  C/C++, Java, HTML/CSS, Flask, Django, Algorithms and Data Structures
- 📊 Data Visulization: PowerBi, MS Excel, Tableau
- 📚 Modeling: Logistic regression, linear regression, decition trees
- 🗄️ Databases:  MongoDB, MySQL, NoSQL
"""
)
st.write('\n')
st.subheader("Soft Skills")
st.write("---")
st.write(
    """
- Leadership
- Decision making
- Teamwork
- Problem solving

"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")





# --- JOB 1
st.write("🚧", "**Code clause | Data Science Intern**")
st.write("June 2023-Present, WFH")
st.write(
    """
Worked on projects like Market-based analysis, Churn Prediction,
and Resume Parser using NLP and Machine Learning
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Coincent /Machine Learning Intern**")
st.write("October 2021-December 20221, WFH")
st.write(
    """
Worked on Projects like news classification, Product Classification
"""
)


# --- Certificates
st.write('\n')
st.subheader("CERTIFICATES")
st.write("---")
for certificate, link in CERTIFICATES.items():
    st.write(f"[{certificate}]({link})")	


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
