import streamlit as st
import base64

    
# ----- Page configs (tab title, favicon) -----
st.set_page_config(
    page_title="Bello Nasiru Aliyu Portfolio",
    page_icon="📊",
)


def home_page():
    # ----- Left menu -----
    with st.sidebar:
        st.image("eae_img.png", width=200)
        st.header("Introduction to Programming Languages for Data")
        st.write("###")
        st.write("Final Project - Feb 2025")
        st.write("Author:Bello Nasiru Aliyu")
        st.write("**Instructor:** [Enric Domingo](https://github.com/enricd)")


    # ----- Top title -----
    st.html("""<div style="text-align: center;"><h1 style="text-align: center;">👋 Hi! My name is Bello Nasiru Aliyu</h1></div>""")  # TODO: Add your name


    # ----- Profile image file -----
    profile_image_file_path = "bello.jpg"       # TODO: Upload your profile image to the same folder as this script and update this if it has a different name

    with open(profile_image_file_path, "rb") as img_file:
        img = "data:image/png;base64," + base64.b64encode(img_file.read()).decode()


    # ----- Your Profile Image -----
    st.html(f"""
    <div style="display: flex; justify-content: center;">
        <img src="{img}" alt="Your Name" width="300" height="300" style="border-radius: 50%; object-fit: cover; margin-top: 40px; margin-bottom: 40px;">
    </div>
    """)


    # ----- Personal title or short description -----
    current_role = "Data Analyst"   # TODO: Change this

    st.html(f"""<div style="text-align: center;"><h4><i>{current_role}</i></h4></div>""")

    st.write("##")    # Adding some space


    # ----- About me section -----
    st.subheader("About Me")

    # TODO: Modify and adapt the following lines to your info, you can add or remove some details if you want
    st.write("""
    - 👨‍💻 I am a Data Analyst with a passion for uncovering insights from data and helping businesses make data-driven decisions.

    - 🛩️ prev: Bachelor's degree in Computer Science and 2 years of experience in data analysis and visualization.

    - ❤️ Passionate about machine learning, data visualization, and storytelling with data.

    - 🏂 Enjoy hiking, photography, and exploring new technologies.

    - 📫 How to reach me: bellobn6666@yahoo.com

    - 🏠 Barcelona

    - 🛩️ prev: 6 years of experience with SQL, Python, and front-end development.

    - ❤️ Passionate about continuous learning, problem-solving, and innovation.

    - 🏂 Hobbies include reading, traveling, and playing chess.

    - 📫 How to reach me: bellobn6666@yahoo.com
    - 🏠 Barcelona
    """)

    # Feel free to add other points like your Linkedin, Github, Social Media, etc.


# This is ensambling the entire app with the different pages and the navigation menu
pg = st.navigation([
    st.Page(home_page, title="Home", icon="👋"),
    st.Page("pages/01_image_cropper.py", title="Image Cropper", icon="🖼️"),
    st.Page("pages/02_netflix_data_analysis.py", title="Netflix Data Analysis", icon="🎬"),
    st.Page("pages/03_temperatures_dashboard.py", title="Temperatures Dashboard", icon="🌦️"),
])
pg.run()