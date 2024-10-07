import streamlit as st
import requests

def display_food_viewer():

    product_name = st.sidebar.text_input("Enter a food product name:", key="food_input")
    try:
        if st.sidebar.button("Get Product Data", key="get_product_button"):
            if product_name:
                search_and_display_products(product_name)
            else:
                st.warning("Please enter a product name before searching.")
    except:
        st.warning("please enter a name before searching")

def search_and_display_products(product_name):
    # API endpoint for searching products
    url = f"https://world.openfoodfacts.org/cgi/search.pl?search_terms={product_name}&json=true"
    
    # Make the API request
    response = requests.get(url)
    data = response.json()
    
    # Check if products were found
    if data['products']:
        display_products(data['products'][:10])  # Display top 10 results
    else:
        st.write("No products found.")

def display_products(products):
    st.write(f"Found {len(products)} similar products (showing top 10).")
    for index, product in enumerate(products):
        display_product(index, product)

def display_product(index, product):
    st.subheader(f"Product {index + 1}: {product.get('product_name', 'No Name Found')}")
    
    # Display the product image
    if 'image_url' in product:
        st.image(product['image_url'], caption=product.get('product_name', 'No Image'))
    
    # Display basic product information
    st.write(f"**Brand**: {product.get('brands', 'N/A')}")
    st.write(f"**Quantity**: {product.get('quantity', 'N/A')}")
    st.write(f"**Categories**: {product.get('categories', 'N/A')}")
    
    display_nutritional_info(product)
    display_ingredients(product)
    
    # Add a horizontal divider for better separation between products
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

if __name__ == "__main__":
    st.title("Food Product Information Viewer")
    display_food_viewer()
