# Food Xense

Food Xense is an innovative web application designed to empower users with personalized nutritional insights, foster a health-conscious community, and provide smart food analysis tools. By leveraging cutting-edge technologies and APIs, Food Xense offers a comprehensive platform for managing dietary habits, discovering healthy recipes, and making informed food choices.

## Features

- **User Authentication**: Secure login and signup functionality.
- **Personalized Profiles**: Users can set dietary preferences, allergies, and health goals.
- **Smart Food Analysis**: 
  - Image recognition for food items
  - Barcode scanning for quick product lookup
  - Detailed nutritional information
- **Community Hub**: 
  - Share and discover healthy recipes
  - Participate in health challenges
  - Engage with other health-conscious individuals
- **AI-Powered Chatbot**: Get instant answers to nutrition-related questions.
- **Meal Planning**: Generate personalized meal plans based on preferences and goals.
- **Health Tracking**: Monitor progress towards personal health objectives.

## Technologies Used

- **Frontend**: Svelte & SvelteKit
- **Backend**: Flask (Python)
- **Database**: Supabase
- **APIs**:
  - Google Gemini API for AI-powered features
  - Open Food Facts API for product information
- **Authentication**: Supabase Auth

## Prerequisites

- Node.js (v14 or later)
- Python (v3.7 or later)
- Supabase account
- Google Cloud account (for Gemini API access)

## Setup and Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/food-xense.git
   cd food-xense
   ```

2. Set up the frontend:
   ```
   cd frontend
   npm install
   ```

3. Set up the backend:
   ```
   cd ../backend
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Create a `.env` file in both the `frontend` and `backend` directories with the following variables:
   ```
   VITE_SUPABASE_URL=your_supabase_url
   VITE_SUPABASE_ANON_KEY=your_supabase_anon_key
   GEMINI_API_KEY=your_gemini_api_key
   ```

5. Start the development servers:
   
   For the frontend:
   ```
   cd frontend
   npm run dev
   ```
   
   For the backend:
   ```
   cd backend
   flask run
   ```

6. Open your browser and navigate to `http://localhost:5000` to view the application.

## Contributing

We welcome contributions to Food Xense! Please read our [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- Thanks to the Open Food Facts community for providing an extensive food product database.
- Gratitude to Google for the Gemini API, enabling advanced AI capabilities in our application.
- Appreciation to the Supabase team for their robust backend-as-a-service platform.

## Contact

For any queries or support, please contact us at support@foodxense.com or open an issue in this repository.

Happy healthy eating with Food Xense! 🥗🍎💪
