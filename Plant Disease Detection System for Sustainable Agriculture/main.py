import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Set page config to wide mode
st.set_page_config(layout="wide", page_title="Plant Disease Detection")

# Custom CSS for styling
st.markdown("""
<style>
    .stButton > button {
        background-color: #2e7d32;
        color: white;
        border: none;
        padding: 0.5rem 1rem;
        border-radius: 5px;
        margin: 0 0.5rem;
        height: auto;
        white-space: normal;
        min-height: 46px;
    }
    .stButton > button:hover {
        background-color: #1b5e20;
    }
    .stButton > button[data-selected="true"] {
        background-color: #1b5e20;
    }
    div[data-testid="stImage"] {
        border-radius: 10px;
        overflow: hidden;
    }
    .prediction-card {
        background-color: #f5f5f5;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .upload-section {
        border: 2px dashed #2e7d32;
        border-radius: 10px;
        padding: 2rem;
        text-align: center;
    }
    .nav-spacer {
        margin-bottom: 2rem;
    }
</style>
""", unsafe_allow_html=True)

def model_prediction(test_image):
    model = tf.keras.models.load_model("trained_plant_disease_model.keras")
    image = tf.keras.preprocessing.image.load_img(test_image, target_size=(128,128))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr])
    predictions = model.predict(input_arr)
    return np.argmax(predictions)

# Initialize session state
if 'current_page' not in st.session_state:
    st.session_state.current_page = "HOME"
if 'prediction_result' not in st.session_state:
    st.session_state.prediction_result = None

# Navigation buttons with better spacing
col1, col2, col3, col4, col5 = st.columns([2, 1.2, 0.6, 1.2, 2])
with col2:
    if st.button("HOME", key="home_btn", 
                use_container_width=True,
                type="primary" if st.session_state.current_page == "HOME" else "secondary"):
        st.session_state.current_page = "HOME"
        st.rerun()

with col4:
    if st.button("DETECT\nDISEASE", key="detect_btn",
                use_container_width=True,
                type="primary" if st.session_state.current_page == "DISEASE DETECTION" else "secondary"):
        st.session_state.current_page = "DISEASE DETECTION"
        st.rerun()

st.markdown('<div class="nav-spacer"></div>', unsafe_allow_html=True)

# Main content
if st.session_state.current_page == "HOME":
    st.markdown("<h1 style='text-align: center;'>Plant Disease Detection System for Sustainable Agriculture</h1>", unsafe_allow_html=True)
    
    # Center the main image using columns
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        img = Image.open("Diseases.png")
        st.image(img, use_container_width=True)
    
    # Add informative text
    st.markdown("""
        <div style='text-align: center; margin-top: 2rem;'>
            <h2>Welcome to our Plant Disease Detection System</h2>
            <p>This advanced system helps farmers and gardeners identify plant diseases quickly and accurately, 
            promoting sustainable agricultural practices and improving crop yields.</p>
        </div>
    """, unsafe_allow_html=True)

else:  # DISEASE DETECTION page
    st.markdown("<h1 style='text-align: center;'>Plant Disease Detection</h1>", unsafe_allow_html=True)
    
    # Create two columns for upload and prediction
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        st.markdown('<div class="upload-section">', unsafe_allow_html=True)
        test_image = st.file_uploader("Choose a plant image to analyze:", key="uploader")
        if test_image:
            st.image(test_image, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="prediction-card">', unsafe_allow_html=True)
        if test_image:
            if st.button("Analyze Image", use_container_width=True):
                with st.spinner('Analyzing image...'):
                    result_index = model_prediction(test_image)
                    
                    class_name = ['Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy',
                                'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew', 
                                'Cherry_(including_sour)___healthy', 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 
                                'Corn_(maize)___Common_rust_', 'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy', 
                                'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 
                                'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot',
                                'Peach___healthy', 'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 
                                'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy', 
                                'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew', 
                                'Strawberry___Leaf_scorch', 'Strawberry___healthy', 'Tomato___Bacterial_spot', 
                                'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold', 
                                'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite', 
                                'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus',
                                'Tomato___healthy']
                    
                    st.session_state.prediction_result = class_name[result_index]
                    st.success("Analysis Complete!")
                
            if st.session_state.prediction_result:
                st.markdown(f"""
                    <div style='text-align: center; margin-top: 1rem;'>
                        <h2>Detection Result</h2>
                        <p style='font-size: 1.2rem; color: #2e7d32; padding: 1rem; background-color: white; 
                        border-radius: 5px; margin: 1rem 0;'>{st.session_state.prediction_result}</p>
                    </div>
                """, unsafe_allow_html=True)
        else:
            st.markdown("""
                <div style='text-align: center;'>
                    <h3>Upload an image to get started</h3>
                    <p>Support for various plant types including:</p>
                    <p>🌱 Apple &nbsp; 🍇 Grape &nbsp; 🌽 Corn &nbsp; 🍅 Tomato</p>
                    <p>🥔 Potato &nbsp; 🫐 Blueberry &nbsp; 🍑 Peach &nbsp; 🫑 Pepper</p>
                </div>
            """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)