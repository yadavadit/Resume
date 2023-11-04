from pathlib import Path
import base64
import streamlit as st
from streamlit_timeline import timeline
# import io
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Aditi_Yadav_Resume.docx"
profile_pic = current_dir / "assets" / "profile-pic.jpeg"
timeline_file = current_dir / "assets" / "timeline.json"
icon = current_dir / "assets" / "ay.jpg"
bg = current_dir / "assets" / "bg.jpg"

image=Image.open(icon)

st.set_page_config(page_title="Aditi Yadav", page_icon=image, layout="wide")

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local(bg)

# Navigation
st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg" style="background-color: #151515;">
  <a class="nav-link" href=" " target="_blank">Aditi Yadav</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item">
        <a class="nav-link" href="#about-me">About Me</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#timeline">Career Snapshot</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#skills">Technical Skillset</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-ex">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#contact">Contact Me</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)


# --- LOAD CSS, PDF & PROFIL PIC ---
# with open(css_file) as f:
#     st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# Custom function for printing text
def txt3(a, b):
  col0, col1, col2 = st.columns([0.5,1,3.5])
  with col1:
    st.markdown('**<span style="color:#27278bff">' + a + '</span>**',unsafe_allow_html=True)
  with col2:
    st.markdown(b)
  
# --- HERO SECTION ---
col1, col2, col3, col4 = st.columns([1.3,1,1.5,1], gap="medium")
with col2:
    st.image(profile_pic, width=250)

with col3:
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("## <span style='color:black'> Aditi Yadav </span>",anchor="title",unsafe_allow_html=True)
    st.write("##### <span style='color:grey'> From walking the runway to coding away, I'm a fashion model and computer engineer who knows how to keep both my wardrobe and code look sharp! </span>",unsafe_allow_html=True)
    st.write("\n")

lcol,rcol = st.columns([1,1.4])
with rcol:
  st.write("📫", "yadav.adit@northeastern.edu")
  st.download_button(
    label=" 📄  Download Resume  📄",
    data=PDFbyte,
    file_name=resume_file.name,
    mime="application/octet-stream",
  )  

# --- SKILLS ---
st.write('\n')
st.write(" ## <span style='color:black'> Technical Skillset :hammer_and_wrench: </span>",anchor="skills",unsafe_allow_html=True)
st.write("---")
txt3('Programming', '`Python` `Javascript` `SQL` `R` `Spark` `Java` `C` `C++`, `HTML`,')
txt3('ML/DL Framework', '`Pandas` `Numpy` `SciPy` `Transformers` `NLTK` `SpaCy` `Scikit-Learn` `Tensorflow` `Keras` `PyTorch` `PyCaret` `H20.ai`')
txt3('Data visualization', '`Matplotlib` `Seaborn` `Plotly` `Altair`, `Ggplot2`')
txt3('BI Tools', '`PowerBI` `Tableau` `Looker`')
txt3('API/Web development', '`Node.js` `Express.js` `React` `Flask` `Django` `FastAPI` `Streamlit` ')
txt3('Cloud/Data Warehouse', '`AWS` `Azure` `GCP` `Databricks` `Snowflake`')
txt3('Business', '`Client Engagement` `Healthcare` `Edtech` `Finance` `Market Research` `Project Scoping` `Proposal Constructions` `Storyboarding`')

# --- WORK HISTORY ---
st.write('\n')
st.write(" ## <span style='color:black'> Work Experience 🧑🏻‍💼</span> ",anchor="work-ex",unsafe_allow_html=True)
st.write("---")

# --- JOB 1
with st.expander("""
👨🏻‍💼 **Data Analyst** 

Northeastern University - MSIS Bridge, September 2023 - Present
</span>
"""):
  st.write(
      """<span style='color:black'>

  - ► Devising marketing strategies to increase student enrollment for Bridge program by analyzing student profiles & demographics & generating Tableau reports to collaborate with cross-functional team

  - ► Identify core, in-demand, and outdated courses using predictive analytics, aligning them with current market & industry opportunities & optimizing staff & resource needs
  
  </span>
  """,unsafe_allow_html=True
  )

# --- JOB 2
with st.expander('''
👨🏻‍💻 **Research Assistant** 

Northeastern University - EDGE, March 2023 - August 2023
'''):
  st.write(
      """<span style='color:black'>

  - ►  Increased annual revenue by **$4 MM** and optimized refill rate by **28%** for **300K** vending machines by providing real-time recommendations based on collaborative filtering and product popularity

  - ►  Built a customer churn model with a **75% recall** and prescriptive reports on Tableau to retain restaurant business

  - ►  Mentored **200+ campus recruits**; supervised training schedules, and designed evaluation framework
  </span>
  """,unsafe_allow_html=True
  )
# --- JOB 3
with st.expander('''
👨🏻‍💻 **Technical Product Engineer** 

Allscripts Healthcare, June 2021 - July 2022
'''):
  st.write(
      """<span style='color:black'>

  - ►  Led a team of 5 in designing over 50 API test cases for Electronic Healthcare microservices

  - ►  Published 10+ customized PowerBI reports, showcasing critical Patient Key Performance Indicators (KPIs) for medical diagnosis

  - ►  Reduced cost by 30% & ensured single-click master job by revamping daily ETL pipelines & parallelizing workflows to fetch structured & unstructured datasets from Azure SQL Server, data marts & Blob storage

  </span>
  """,unsafe_allow_html=True
  )
  # --- JOB 4
with st.expander('''
👨🏻‍💻 **Research Assistant** 

Athens Information Technology, June 2019 - August 2019
'''):
  st.write(
      """<span style='color:black'>

  - ►  Developed a Flask web application prototype using computer vision to detect user emotions & demographics for an age-restricted vending machine, using OpenCV & deep learning techniques such as convolutional neural networks (CNNs)

  </span>
  """,unsafe_allow_html=True
  )

  # --- JOB 5
with st.expander('''
👨🏻‍💻 **Data Analyst-Intern** 

Defence R&D Organization, June 2018 - October 2018
'''):
  st.write(
      """<span style='color:black'>

  - ►  Reduced computation for payroll management system by ~40% by optimizing queries using views & moidying join conditions

  - ►  Developed queries to efficiently fetch data from centralized data warehouse for 10+ financial microservices such as tax deductions & service exemptions

  </span>
  """,unsafe_allow_html=True
  )

  # ---- CONTACT ----
st.write("## <span style='color:purple'> Get In Touch With Me! 👋🏻</span>",anchor="contact",unsafe_allow_html=True)
st.write("---") 

contact_form = """
    <form action="https://formsubmit.co/yadav.adit@northeastern.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
left, mid, right = st.columns([1.5,0.5,1.5])
with left:
    st.markdown(contact_form, unsafe_allow_html=True)
with right:
      st.markdown('''
      <br>
      <h4 style="color:red; text-align:center">
      Social Media📱
      <br><br>

      [LinkedIn](https://www.linkedin.com/in/yaditi/) <br><br>
      [Kaggle](https://www.kaggle.com/yadavadit) <br><br>
      [GitHub](https://github.com/yadavadit)
      </h4>
      ''',unsafe_allow_html=True)

with open(css_file) as f:
  st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

a,b=st.columns([1,1.3])  
with b:
  st.markdown('![Visitor count](https://shields-io-visitor-counter.herokuapp.com/badge?page=https://share.streamlit.io/https://arnabxtech.streamlit.app/label=VisitorsCount&labelColor=000000&logo=GitHub&logoColor=FFFFFF&color=1D70B8&style=for-the-badge)')
