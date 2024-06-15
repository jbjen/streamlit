import streamlit as st

st.title("A Glimpse of Me 👩‍❤️‍")



st.title("📷Self-Representation")


image_paths = ["pict\selfportrait.jpg"]


cols = st.columns(len(image_paths))

for col, image_path in zip(cols, image_paths):
    col.image(image_path)


st.header(" 👧🌹 Dumdumaya , Jerlyn Bermudez")

st.markdown("""
##### 👨‍👩‍👧‍👦Family Members👨‍👩‍👧‍👦 

* 👩‍👦 Mother's Name: Donna Lyn B. Dumdumaya
* 👨‍👧‍👧 Father's Name: Erwin D. Dumdumaya
* 👭🏻 Sister's Name: Erwina B. Dumdumaya          

### 🔎 Overview
""", unsafe_allow_html=True)

# Personal Information
st.header("Personal Information")
st.write("**Name:** Jerlyn B. Dumdumaya")
st.write("**Age:** 21 years old")
st.write("**Education:** Currently studying at CARLOS HILADO MEMORIAL STATE UNIVERSITY")
st.write("**Year:** 3rd year Bachelor of Science in Information Systems Student")
st.write("**Location:** So. Dapdap Brgy Lantad Silay City")

with st.expander("Who am I 10 years From now??"):
    st.markdown("""
    
    #
Ten years from now, I imagine myself as a successful business owner. I won't be working directly with my degree in Information Systems, 
                but I'll use my skills in data analysis, software development, and problem-solving to create something new. I see myself 
                running a successful business that combines my love for technology with my creative side, maybe in digital art or interactive storytelling. 
                My business will not only make me financially stable but also help people through technology.
    """, unsafe_allow_html=True)

# Quotes
st.header("Favorite Quotes")
st.write("1. *\"Find out who you are and be that person. That's what your soul was put on this earth to be. Find that truth, live that truth, and everything will fall into place.\"*")
st.write("2. *\"The greatest glory in living lies not in never falling, but in rising every time we fall.\"*")
st.write("3. *\"You will face many defeats in life, but never let yourself be defeated.\"*")





import streamlit as st

images = [
    {"path": "pict\\friend3.jpg", "caption": "Academic years are often described as some of the most formative and challenging times in a person's life. The journey through education is filled with hurdles, demanding tasks, and moments of self-doubt. However, amidst the pressures of exams, projects, and deadlines, the presence of supportive friends and classmates plays an important role in not only making the experience bearable but also enriching and enjoyable. From the very first day of school, friendships begin to form. These bonds, initially built on shared classes and common interests, soon evolve into deeper relationships that provide a reliable support system. Friends and classmates become a source of encouragement, helping each other navigate through the hardships of academic life. Whether it's offering a listening ear after a tough day, sharing notes for a missed lecture, or providing motivation before a big exam, their presence is invaluable."},
    {"path": "pict\\friend2.jpg", "caption": "Having close friends around you is incredibly valuable. They offer emotional support, understanding, and companionship through life's challenges and joys. These relationships give you a sense of belonging and help you feel stable and secure. Close friends listen to you without judging, comfort you in tough times, and celebrate your successes, making life more enjoyable and meaningful. Their constant presence and empathy help you face difficulties with confidence, ensuring you never feel alone."},
    {"path": "pict\\friend1.jpg", "caption": "Having supportive friends and classmates during my academic years has been essential for my success and enjoyment in school. Their encouragement, inspiration, and companionship have turned what could have been daunting challenges into opportunities for personal growth and fun. As I navigate through my studies, the bonds I've formed with my peers give me the strength, motivation, and joy I need to keep pushing forward and excel. These relationships are not just crucial for my academic achievements; they also help shape me into a more well-rounded, resilient, and compassionate individual ready to contribute to society."}
]

st.title("🖼️ Gallery")
st.write("Welcome to my gallery! Here are some moments with my friends during my academic years, highlighting the importance of friendship and support.")

for image in images:
    st.image(image["path"], caption=image["caption"])


st.markdown(
    """
    <style>
    .stApp {
        background-color: #95D2B3;
        padding: 2em;
    }
    h1, h2 {
        color: #254336;
    }
    .stText {
        font-size: 1.5em;
        color: #151515;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Footer or additional sections (optional)
st.write("### Thank you for visiting my profile!")
st.write("Feel free to connect and reach out if you share similar interests or have any questions.")