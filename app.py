import os
import gradio as gr
from openai import OpenAI

# Get API key from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if OPENAI_API_KEY is None:
    raise ValueError("API Key not set in environment variables.")

client = OpenAI(api_key=OPENAI_API_KEY)

def get_recommendations(books_input):
    # Split the input by line and format the books
    books = books_input.splitlines()
    
    if not books:
        return "Please enter at least one book."
    
    # Build the prompt by processing the books
    prompt = "I’ve read and deeply enjoyed the following books:\n\n"
    for book in books:
        # Split the book into title and author
        try:
            title, author = book.split(" by ")
            prompt += f"- {title} by {author}\n"
        except ValueError:
            return "Please enter books in the format 'Title by Author'. For example, 'Hamnet by Maggie O'Farrell'."
    
    prompt += (
        "\nBased on this list, please analyze the emotional, thematic, and stylistic threads "
        "that tie these books together. Then, recommend five other books I am likely to enjoy "
        "on a similarly profound level. For each recommendation, include:\n"
        "- A brief synopsis\n"
        "- An explanation of why you believe it fits my taste\n"
        "- Which of my previously read books it most closely resonates with and why\n"
        "Prioritize introspective storytelling, beautiful prose, and emotional depth over genre similarity."
    )

    # Get recommendations from OpenAI API
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a literary assistant who gives deeply personalized book recommendations."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.8
    )

    return response.choices[0].message.content

with gr.Blocks(title="📚 Book Recommender AI") as demo:
    gr.Markdown("# 📖 Personalized Book Recommender\nEnter your favorite books to get deep, thoughtful recommendations.")
    
    with gr.Row():
        input_books = gr.Textbox(
            label="📚 Paste Your Favorite Books (One per Line)",
            lines=10, 
            placeholder='Hamnet by Maggie O\'Farrell\nThe Midnight Library by Matt Haig'
        )
    
    with gr.Row():
        recommend_btn = gr.Button("✨ Recommend Books")
    
    output = gr.Textbox(label="🔍 Recommendations", lines=20)

    recommend_btn.click(fn=get_recommendations, inputs=input_books, outputs=output)

demo.launch()
