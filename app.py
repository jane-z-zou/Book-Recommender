import os
import requests
import gradio as gr

# Get Hugging Face API key from environment variables
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
if HUGGINGFACE_API_KEY is None:
    raise ValueError("Hugging Face API Key not set. Set it using 'export HUGGINGFACE_API_KEY=your_key_here'")

API_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"
HEADERS = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}

def query_huggingface(prompt):
    response = requests.post(
        API_URL,
        headers=HEADERS,
        json={"inputs": prompt, "parameters": {"max_new_tokens": 1000}}  # Adjust if needed
    )
    if response.status_code != 200:
        return f"❌ Error {response.status_code}: {response.text}"
    return response.json()[0]["generated_text"]

def get_recommendations(books_input):
    books = books_input.strip().splitlines()
    if not books:
        return "⚠️ Please enter at least one book in the format: Title by Author"

    prompt = "I’ve read and deeply enjoyed the following books:\n\n"
    for book in books:
        try:
            title, author = book.split(" by ")
            prompt += f"- {title} by {author}\n"
        except ValueError:
            return "⚠️ Format error. Please use 'Title by Author' on each line."

    prompt += (
        "\nBased on this list, recommend 5 books I’ll love 🧡. Keep responses SHORT (3-4 lines per book), include emojis 🎯📚✨, and skip long analysis.\n"
        "For each book, give:\n"
        "1. A quick blurb or vibe 🎭\n"
        "2. Why it matches my taste 🧠\n"
        "3. A similar book I’ve read 📖\n"
        "Make it warm, fun, and human — like a friend texting recs 💬💡"
    )

    return query_huggingface(prompt)

with gr.Blocks(title="📚 Book Recommender AI (Free Edition)") as demo:
    gr.Markdown("## 📖 Personalized Book Recommender\nEnter a few of your favorite books to get cozy, emoji-filled suggestions 💬📚✨")
    
    input_box = gr.Textbox(lines=10, placeholder="e.g.\nHamnet by Maggie O'Farrell\nA Psalm for the Wild-Built by Becky Chambers", label="📚 Your Favorite Books")
    output_box = gr.Textbox(lines=20, label="🔍 Recommendations")
    generate_button = gr.Button("✨ Recommend Books")

    generate_button.click(get_recommendations, inputs=input_box, outputs=output_box)

demo.launch()
