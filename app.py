import gradio as gr
import json
from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def get_recommendations(book_json_text):
    try:
        book_list = json.loads(book_json_text)
        if not isinstance(book_list, list):
            return "Invalid format: Please provide a list of books in JSON."
    except json.JSONDecodeError:
        return "Invalid JSON. Please check your formatting."

    prompt = "I’ve read and deeply enjoyed the following books:\n\n"
    for book in book_list:
        prompt += f"- {book['title']} ({book['rating']} stars): {book['notes']}\n"
    
    prompt += (
        "\nBased on this list, please analyze the emotional, thematic, and stylistic threads "
        "that tie these books together. Then, recommend five other books I am likely to enjoy "
        "on a similarly profound level. For each recommendation, include:\n"
        "- A brief synopsis\n"
        "- An explanation of why you believe it fits my taste\n"
        "- Which of my previously read books it most closely resonates with and why\n"
        "Prioritize introspective storytelling, beautiful prose, and emotional depth over genre similarity."
    )

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
    gr.Markdown("# 📖 Personalized Book Recommender\nUpload or paste your favorite books to get deep, thoughtful recommendations.")
    
    with gr.Row():
        input_json = gr.Textbox(label="📚 Paste Your Book List (in JSON)", lines=15, placeholder='[{"title": "Hamnet", "rating": 5, "notes": "emotional, poetic, historical"}]')
    
    with gr.Row():
        recommend_btn = gr.Button("✨ Recommend Books")
    
    output = gr.Textbox(label="🔍 Recommendations", lines=20)

    recommend_btn.click(fn=get_recommendations, inputs=input_json, outputs=output)

demo.launch()
