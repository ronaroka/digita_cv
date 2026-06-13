import streamlit as st
from PIL import Image

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | "
PAGE_ICON = ":wave:"
NAME = "Rona Roka"
DESCRIPTION = """
Physics teacher with a master's degree in physics trying to get inyo data analytics and data science.
"""

EMAIL = "ronaroka98@gmail.com"
LINKEDIN_URL = "https://www.linkedin.com/in/rona-roka"
GITHUB1_URL = "https://github.com/sofa-framework/sofa"

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# Directly reference files in the assets folder (ensure it exists)
resume_file = "assets/cv template.pdf"
profile_pic_file = "assets/Rona foto profili.jpg"

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

profile_pic = Image.open(profile_pic_file)

# Sidebar navigation
page = st.sidebar.radio("Navigate", ["Home", "About", "Projects"])

if page == "Home":
    # --- HERO SECTION ---
    col1, col2 = st.columns([1, 2], gap="small")
    with col1:
        st.image(profile_pic, width=230)

    with col2:
        st.title(NAME)
        st.write(DESCRIPTION)
        st.download_button(
            label="📄 Download Resume",
            data=PDFbyte,
            file_name="CV.pdf",
            mime="application/octet-stream",
        )

    # --- EXPERIENCE & QUALIFICATIONS ---
    st.write("\n")
    st.subheader("Experience & Qualifications")
    st.write(
        """
- ✔️ Physics Teacher (Grades 7–9) covering mechanics, electricity, thermodynamics, and exam prep.
- ✔️ Research in medical physics focusing on radiation dose evaluation in diagnostic procedures.
- ✔️ Social Media Management: Experienced in managing profiles and developing content.
"""
    )

    # --- SKILLS ---
    st.write("\n")
    st.subheader("Hard Skills")
    st.write(
        """
- 👩‍💻 Radiation dosimetry & medical physics analysis
- 📊 Basic digital marketing tools and concepts
- 🗄️ Physics problem solving at advanced level
- 🤖 Developed and delivered engaging and comprehensive lesson plans
"""
    )

    # --- WORK HISTORY ---
    st.write("\n")
    st.subheader("Work History")
    st.write("---")

    # --- JOB 1
    st.write("🚧", "**Renewable Energy Intern | Ministry of Economy, Prishtina**")
    st.write("2023 - 2023")
    st.write(
        """
- ► Conducted research on energy efficiency and renewable resources.
- ► Translated and commented on documents and laws.
"""
    )

    # --- JOB 2
    st.write("\n")
    st.write("🚧", "**Physics Teacher | Gjakova**")
    st.write("2023-Ongoing")
    st.write(
        """
- ► Maintained detailed records of student attendance, grades, and progress.
- ► Developed and delivered engaging and comprehensive lesson plans for Physics classes.
- ► Plepared students for the physics Olympiad showing success up to the national level.
"""
    )

    

elif page == "About":
    st.title("About Me")
    st.write("""
    I am a Physics Teacher with experience teaching grades 7–9,
    focusing on core topics such as mechanics, electricity,
    thermodynamics, and exam preparation. I hold an MSc in Physics
    and have completed my master’s studies in the field.
    My students have achieved strong results in physics olympiads,
    reflecting the effectiveness of my teaching approach and their dedication.
    I have also been involved in applied medical physics research related to
    radiation dose evaluation in diagnostic procedures. Alongside my academic
    and teaching work, I have basic knowledge of digital marketing concepts and tools,
    which I am interested in developing further.

    """)

elif page == " Projects":
    st.title("My projects")
    st.subheader("🔬 Physics Simulation App")
    st.write("A simple app that demonstrates the free fall concept")
    st.write("Tools used: Python & Streamlit")
    st.write(f"🔗 Check this project on [GitHub]({GITHUB1_URL}).")

    st.markdown("---")

    st.subheader("🏎️ Motion calculator")
    st.write("An app that calculates motion of objects")
    st.write("Tools used: Python & Streamlit")
    st.write(f"🔗 Check this project on [GitHub]({GITHUB1_URL}).")


    # Show LinkedIn and Email only on the About page
    st.write("📫", EMAIL)
    st.write(f"Feel free to connect with me on [LinkedIn]({LINKEDIN_URL}).")