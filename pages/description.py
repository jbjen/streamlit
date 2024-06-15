import streamlit as st

st.title("Description of Different Streamlit Application")


st.header('Machine Learning Compiled Application')
st.image(".\pict\emotions.png")

with st.expander("😊 Emotion Detector 😊"):
    st.markdown("""
    
    #
                An Emotion Analyzer 
An emotion analyzer using text in machine learning reads text and breaks it down to understand feelings. 
                It learns from examples where emotions like happiness, sadness, or anger are labeled. 
                Using these examples, it trains computer models to spot patterns in how words and sentences express these emotions.
                 After training, the analyzer checks how well it can guess emotions in new texts. 
                It helps with understanding opinions, evaluating customer feedback, and even monitoring emotions in text for mental health purposes.

                
    """, unsafe_allow_html=True)

st.header('🦁 Image Classification 🐆')
st.image(".\pict\imageclassify.png")

with st.expander("Image Classification of Wild Cats"):
    st.markdown("""
    
    #
                In image classification using machine learning, like with your wild cats dataset, the process involves teaching a computer to recognize and categorize images. 
                You start by gathering lots of pictures of wild cats, such as lions, tigers, and cheetahs. The images of wild cats are first collected and then processed for machine learning.
                 They're transformed into data that the computer can interpret. Then, a machine learning model is trained on this data to recognize and classify different types of wild cats.
                Once trained, the model can predict the type of wild cat in new images it hasn't seen before.
    """, unsafe_allow_html=True)

st.header('🔍Prediction')
st.image(".\pict\predict1.png")
st.image(".\pict\predict2.png")

with st.expander("🌦️ Weather Predictor 🌦️"):
    st.markdown("""
    
    In weather prediction using machine learning, we download datasets from sources like Kaggle, which provide historical data on temperature, humidity, wind speed, and atmospheric pressure. 
                These datasets are then fed into machine learning algorithms such as decision trees or random forests. The algorithms analyze past weather patterns to learn relationships between these variables and outcomes like rain or sunshine. 
                By training on historical data, the models can forecast future weather conditions. This technology is crucial for predicting weather patterns, offering insights beneficial for agriculture, disaster management, and daily planning.
                         
    """, unsafe_allow_html=True)