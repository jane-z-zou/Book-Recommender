# 📚 Jane's Book Recommender

Welcome to your new favorite cozy, emoji-filled AI app that gives emotionally resonant book recommendations based on your personal favorites.

This is a little book bot I made using the free Hugging Face Inference API (Zephyr model). Just tell it the books you’ve loved (in the format "Title by Author") and it’ll suggest five new reads with a fun, friendly tone. Perfect if you're someone who loves introspective, well-written stories and wants recs that feel right, not just match the genre.

I built this because I’m the kind of person who finishes a book, stares at the ceiling, and spirals a bit wondering what to read next. I wanted something simple and warm, like getting a thoughtful recommendation from a good friend over text.

## 🚀 Demo

👉 [Launch the App on Hugging Face Spaces](https://huggingface.co/spaces/your-username/book-recommender-ai)

## 🧠 How It Works

1. Clone this repo or download the files
2. Run app.py locally or deploy to Hugging Face Spaces
3. Paste your favorite books in the text box (format: Title by Author)
4. Click the button and get your personalized recs!

This application utilizes the [HuggingFaceH4/zephyr-7b-beta](https://huggingface.co/HuggingFaceH4/zephyr-7b-beta) language model via the Hugging Face Inference API. By analyzing the themes, styles, and emotional tones of your listed books, it generates personalized recommendations that resonate with your reading preferences.

## 🛠️ Installation

To run the app locally:

1. **Clone the Repository**:

   ```bash
   git clone https://huggingface.co/spaces/zoujane/book-recs
   ```

2. **Install Dependencies**:

   Ensure you have Python 3.8 or higher installed. Then, install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set the Hugging Face API Key**:

   Obtain your Hugging Face API key from [your account settings](https://huggingface.co/settings/tokens) and set it as an environment variable:

   ```bash
   export HUGGINGFACE_API_KEY=your_api_key_here
   ```

4. **Run the Application**:

   ```bash
   python app.py
   ```

   The app will launch in your default web browser.

## 📂 Project Structure

```
book-recommender-ai/
├── app.py              # Main application script
├── requirements.txt    # List of dependencies
└── README.md           # Project documentation
```

## 📄 Requirements

- Python 3.8 or higher
- [Gradio](https://gradio.app/)
- [Requests](https://docs.python-requests.org/)

Install all dependencies using:

```bash
pip install -r requirements.txt
```

## 📜 License

This project is licensed under the Apache License 2.0.
