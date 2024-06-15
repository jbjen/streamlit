import streamlit as st
from st_pages import Page, Section, show_pages, add_page_title, hide_pages

add_page_title()
show_pages(
    [   
        Page("home.py", "Machine Learning Techniques", "👩"),
        Section("Developing Applications Using Various Machine Learning Techniques",),
        Page("pages/aboutme.py", " 🙋 A Glimpse of Me ", "1️⃣", in_section=True),
        Page("pages/description.py", "📲 Specifications of the Application", "2️⃣", in_section=True),
        Page("pages/itqmtlearnings.py", "Insights Gained from the Subject", "3️⃣", in_section=True),
    
  
        Section("PROJECTS", "💾"),
        Page("pages/prediction.py", "🌦️ Weather Predictor 🌦️", "1️⃣", in_section=True),
        Page("pages/sentimentemotion.py", "😊 Emotion Detector 😊", "2️⃣", in_section=True),
        Page("pages/imageclassifier.py", "🦁 Image Classification for Wild Cats 🐆", "3️⃣", in_section=True),


         Section("SOURCE CODE", "📄"),
        Page("pages/prediction_src.py", "Prediction", "1️⃣", in_section=True),
        Page("pages/sentimentemotionanalyzer_src.py", "Emotion Detector", "2️⃣", in_section=True),
        Page("pages/imageclassifier_src.py", "Image Classification", "3️⃣", in_section=True),
    

    ]
)

hide_pages(["Thank you"])

# Display additional content
st.markdown("### 👨‍🔧 Machine Learning Exploration by [Jerlyn](https://github.com/koalatech)")

# Display an image
st.image("./pict/ml.jpg")

# Display info box
st.info("⚙️🤖 This application demonstrates how different machine learning techniques can be used in quality management to improve our work and efficiency as students..")

# Display divider
st.markdown("---")




# Display another image
st.image("./pict/mlearning.jpg")

# Display more markdown content
st.markdown("""
Machine learning is transforming various industries by enabling companies to analyze large datasets quickly and accurately. It enhances operations in sectors such as healthcare, finance, manufacturing, and even educational institutions. 
            By improving efficiency, reducing costs, and enhancing student outcomes, machine learning techniques like deep learning and natural language processing are driving innovation and shaping the future of education. 
            As schools and universities adopt these technologies, they pave the way for smarter automation and data-driven decision-making, crucial for achieving academic excellence and institutional success in today's evolving landscape.

### 🌟🌟🌟🌟🌟 Star the project on Github  
<iframe src="https://ghbtns.com/github-btn.html?user=koalatech&repo=streamlit_web_app&type=star&count=true"  width="150" height="20" title="GitHub"></iframe>
""", unsafe_allow_html=True)

# Add CSS to hide Streamlit menu and footer
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Additional custom styles
custom_styles = """
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
"""
st.markdown(custom_styles, unsafe_allow_html=True)
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
