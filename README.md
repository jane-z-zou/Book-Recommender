# 📚 Jane's Book Recommender

Welcome to Book Recommender AI—your personal literary assistant that suggests books based on your favorites. Simply input a list of books you've enjoyed, and receive curated recommendations complete with brief synopses! ✨📖💬

I built this little tool because I was tired of getting soulless book recs that just matched genres. I wanted something that felt more like a friend saying, “If you loved Hamnet, you’re going to cry over this one too 🥲.” I’ve read a lot of emotionally resonant books that stuck with me, and I wanted an AI that could understand why they moved me, not just that they were "literary fiction."

This app is powered by Zephyr-7B, one of Hugging Face’s free and friendly open-source models. It keeps things short, cozy, and fun—like texting a bookish pal with great taste. Perfect for introspective readers who care more about vibe and voice than bestseller lists.

## 🚀 Demo

👉 [Launch the App on Hugging Face Spaces](https://huggingface.co/spaces/your-username/book-recommender-ai)

## 🧠 How It Works

This application utilizes the [HuggingFaceH4/zephyr-7b-beta](https://huggingface.co/HuggingFaceH4/zephyr-7b-beta) language model via the Hugging Face Inference API. By analyzing the themes, styles, and emotional tones of your listed books, it generates personalized recommendations that resonate with your reading preferences.

## ✍️ Usage

1. **Enter Your Favorite Books**: Provide a list of books you've enjoyed, each in the format: `Title by Author`. For example:

   ```
   Hamnet by Maggie O'Farrell
   The Overstory by Richard Powers
   ```

2. **Generate Recommendations**: Click the "✨ Recommend Books" button.

3. **Receive Suggestions**: The app will display five book recommendations, each with a brief description and relevant emojis to capture the essence of the book.

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

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
