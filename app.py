import streamlit as st
import google.generativeai as genai
from PIL import Image
import io
from foodXense import display_food_viewer  # Product search functionality

# Configure the Gemini API
GEMINI_API_KEY=st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=GEMINI_API_KEY) # Replace with your actual API key
model = genai.GenerativeModel("gemini-1.5-flash")

# Function to analyze an image and detect objects using the Gemini API
def analyze_image(image):
    prompt = "Analyze the image and detect objects, especially food items. List the detected objects."
    response = model.generate_content([image, prompt])
    return response.text

# Function to get food recommendations or recipes based on analysis
def get_food_recommendations(detected_items):
    prompt = f"Based on the following detected food items: {detected_items}, suggest food recommendations or recipes."
    response = model.generate_content([prompt])
    return response.text

# Streamlit app configuration
st.title("Advanced Food App: Image Analysis, Reviews, and Recommendations")

# Sidebar options for choosing between different input methods
input_method = st.sidebar.radio(
    "Select input method",
    ("Upload Food Image", "Capture from Camera", "Search for Product")
)

image = None

# Image upload option
if input_method == "Upload Food Image":
    uploaded_file = st.sidebar.file_uploader("Upload an image (JPG, PNG, or SVG):", type=["jpg", "jpeg", "png", "svg"])
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

# Camera capture option
elif input_method == "Capture from Camera":
    img_file_buffer = st.sidebar.camera_input("Take a picture")
    if img_file_buffer:
        bytes_data = img_file_buffer.getvalue()
        image = Image.open(io.BytesIO(bytes_data))
        st.image(image, caption="Captured Image", use_column_width=True)

# Food product search option using Open Food Facts API
elif input_method == "Search for Product":
    display_food_viewer()  # Displays the food search functionality from the external module

# Analyze image and get food recommendations
if image is not None:
    if st.button("Analyze Image"):
        # Analyze image using Gemini API
        detected_items = analyze_image(image)
        st.subheader("AI Detected Food Items:")
        st.write(detected_items)

        # Get food recommendations and recipes
        recommendations = get_food_recommendations(detected_items)
        st.subheader("Food Recommendations & Recipes:")
        st.write(recommendations)

        # Allow user to submit their own review for the analyzed image
        st.subheader("Share Your Review:")
        user_review = st.text_area("Write a review of the food or product shown in the image:")
        if st.button("Submit Review"):
            st.success("Thank you for your review!")
            # Here, you can add functionality to store the review in a database

if input_method == "Search for Product":
    display_food_viewer()  
else:
    if input_method in ["Upload Food Image", "Capture from Camera"]:
        st.error("Please upload or capture an image to analyze in the sidebar.")
