# 🍽️ Food Xense: Your Personalized Nutrition Journey

Welcome to Food Xense, your one-stop shop for smarter food choices and a healthier lifestyle!

Imagine:

- Snapping a picture of your meal and instantly getting a detailed nutritional breakdown. 📸
- Discovering delicious recipes tailored to your dietary needs and preferences. 🍲
- Connecting with a community of like-minded individuals for support and motivation. 🤝
- Getting personalized meal plans that fit your goals. 💪

Food Xense makes this possible!

## 🌟 Here's what makes us special:

- **Smart Food Analysis**:
  - Image recognition: Upload a photo of your food, and we'll analyze it for you!
  - Barcode scanning: Scan a barcode, and we'll instantly tell you everything you need to know about that product.
  - Detailed nutrition information: Calories, macros, vitamins, and more – all at your fingertips.
- **Personalized Profiles**: Tell us about yourself – your allergies, preferences, and health goals – so we can tailor our recommendations just for you!
- **Community Hub**: Join a supportive community of individuals who share your passion for healthy eating. Share recipes, participate in challenges, and get motivated together.
- **AI-Powered Chatbot**: Have any questions about nutrition? Our AI chatbot is here to help! 🤖
- **Meal Planning**: Get personalized meal plans that are easy to follow and delicious!
- **Health Tracking**: Monitor your progress and stay on track with your health goals. 📈

## 🚀 Tech Stack

- Frontend: Svelte
- Backend: Flask
- Database: Supabase
- AI Integration: Google Gemini API
- Food Data: Open Food Facts API

## 🏁 Getting Started

Ready to take your nutrition journey to the next level? Here's how to get started:

1. **Clone the repo**:
   ```
   git clone https://github.com/yourusername/food-xense.git
   cd food-xense
   ```

2. **Set up the frontend**:
   ```
   cd frontend
   npm install
   ```

3. **Set up the backend**:
   ```
   cd ../backend
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

4. **Set up your environment variables**:
   Create a `.env` file in both the frontend and backend directories.
   Add the following variables:
   ```
   VITE_SUPABASE_URL=your_supabase_url
   VITE_SUPABASE_ANON_KEY=your_supabase_anon_key
   GEMINI_API_KEY=your_gemini_api_key
   ```

5. **Start the development servers**:
   
   Frontend:
   ```
   cd frontend
   npm run dev
   ```
   
   Backend:
   ```
   cd backend
   flask run
   ```

6. Open your browser and visit `http://localhost:5000` to explore Food Xense!

## 🤝 Contributing

We're always looking for ways to improve Food Xense!

- **Contribute**: Check out our `CONTRIBUTING.md` file for details on how you can get involved.
- **Contact**: Reach out to us at support@foodxense.com or open an issue on our repository.

Let's make healthy eating a delicious adventure! 🥗🍎💪
