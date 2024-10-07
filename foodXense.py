import streamlit as st
import google.generativeai as genai
from PIL import Image
import io
import requests

# Configure the Gemini API
GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

def fetch_product_data(product_name):
    url = f"https://world.openfoodfacts.org/cgi/search.pl?search_terms={product_name}&json=true"
    response = requests.get(url)
    return response.json()

def display_product_list(products):
    st.write(f"Found {len(products)} similar products (showing top 10).")
    for index, product in enumerate(products[:10]):
        display_single_product(index, product)

def display_single_product(index, product):
    st.subheader(f"Product {index + 1}: {product.get('product_name', 'No Name Found')}")
    
    if 'image_url' in product:
        st.image(product['image_url'], caption=product.get('product_name', 'No Image'))
    
    st.write(f"**Brand**: {product.get('brands', 'N/A')}")
    st.write(f"**Quantity**: {product.get('quantity', 'N/A')}")
    st.write(f"**Categories**: {product.get('categories', 'N/A')}")
    
    display_nutritional_info(product)
    display_ingredients(product)
    
    st.write("---")

def display_nutritional_info(product):
    if 'nutriments' in product:
        st.write("### Nutritional Information (Basic):")
        nutriments = product['nutriments']
        st.write(f"Energy: {nutriments.get('energy-kcal_100g', 'N/A')} kcal/100g")
        st.write(f"Fat: {nutriments.get('fat_100g', 'N/A')} g/100g")
        st.write(f"Carbohydrates: {nutriments.get('carbohydrates_100g', 'N/A')} g/100g")
        st.write(f"Proteins: {nutriments.get('proteins_100g', 'N/A')} g/100g")
    else:
        st.write("Nutritional information not available.")

def display_ingredients(product):
    st.write("### Ingredients:")
    if 'ingredients_text' in product:
        st.write(product['ingredients_text'])
    else:
        st.write("Ingredients not available.")

def product_search_interface():
    st.title("Food Product Information Viewer")
    
    product_name = st.sidebar.text_input("Enter a food product name:", key="food_product_name_input")
    
    if st.sidebar.button("Get Product Data", key="get_product_button"):
        if product_name:
            data = fetch_product_data(product_name)
            if data['products']:
                display_product_list(data['products'])
            else:
                st.write("No products found.")
        else:
            st.warning("Please enter a product name before searching.")

def analyze_image_content(image):
    prompt = "Analyze the image and detect objects, especially food items. List the detected objects."
    response = model.generate_content([image, prompt])
    return response.text

def generate_food_recommendations(detected_items):
    prompt = f"Based on the following detected food items: {detected_items}, suggest food recommendations or recipes."
    response = model.generate_content([prompt])
    return response.text

def main():
    st.title("Advanced Food App: Image Analysis, Reviews, and Recommendations")

    input_method = st.sidebar.radio(
        "Select input method",
        ("Upload Food Image", "Capture from Camera", "Search for Product")
    )

    if input_method == "Upload Food Image":
        image = handle_image_upload()
    elif input_method == "Capture from Camera":
        image = handle_camera_capture()
    elif input_method == "Search for Product":
        product_search_interface()
        return

    if image:
        display_image(image)
        if st.button("Analyze Image"):
            process_image(image)
    else:
        st.error("Please upload or capture an image to analyze.")

def handle_image_upload():
    uploaded_file = st.sidebar.file_uploader("Upload an image (JPG, PNG, or SVG):", type=["jpg", "jpeg", "png", "svg"])
    if uploaded_file:
        return Image.open(uploaded_file)
    return None

def handle_camera_capture():
    img_file_buffer = st.sidebar.camera_input("Take a picture")
    if img_file_buffer:
        bytes_data = img_file_buffer.getvalue()
        return Image.open(io.BytesIO(bytes_data))
    return None

def display_image(image):
    st.image(image, caption="Uploaded/Captured Image", use_column_width=True)

def process_image(image):
    detected_items = analyze_image_content(image)
    st.subheader("AI Detected Food Items:")
    st.write(detected_items)

    recommendations = generate_food_recommendations(detected_items)
    st.subheader("Food Recommendations & Recipes:")
    st.write(recommendations)

    st.subheader("Share Your Review:")
    user_review = st.text_area("Write a review of the food or product shown in the image:")
    if st.button("Submit Review"):
        st.success("Thank you for your review!")
        # Here, you can add functionality to store the review in a database

if __name__ == "__main__":
    main()
