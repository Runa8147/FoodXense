# Advanced Food Analysis and Recommendation App

This application is built with **Streamlit** and **Google Gemini API** to analyze images, search for food products, and provide food recommendations or recipes. It uses the Open Food Facts API for food product searches and allows users to share reviews for products.

## Features

- Upload or capture images to analyze food items.
- Search for food products using the Open Food Facts API.
- Receive food recommendations or recipes based on image analysis.
- Submit reviews for food products.
  
## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/foodXense.git
    cd foodXense
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up your secret variables for the Google Gemini API:
    - Create an `secrets.toml` file in the .streamlit directory and add your Google Gemini API key:
      ```bash
      GOOGLE_API_KEY=your_google_gemini_api_key
      ```

5. Run the app:
    ```bash
    streamlit run app.py
    ```

## File Structure

```bash
.
├── __pycache__/               # Compiled Python files
├── .streamlit/                # Streamlit configuration files
    ├── secrets.toml               # Secrets configuration file
├── app.py                     # Main application file
├── foodXense.py               # Contains the Open Food Facts API search functionality
├── README.md                  # Project documentation
├── requirements.txt           # List of Python dependencies
├── .gitignore                 # Files and directories to ignore in version control
                  # Environment variables (not tracked by git)
