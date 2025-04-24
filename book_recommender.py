import os
import requests

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
        json={"inputs": prompt, "parameters": {"max_new_tokens": 1500}}
    )
    if response.status_code != 200:
        return f"Error: {response.status_code} - {response.text}"
    return response.json()[0]["generated_text"]

def get_recommendations(books_input):
    books = books_input.strip().splitlines()
    if not books:
        return "Please enter at least one book in the format: Title by Author"

    prompt = "I’ve read and deeply enjoyed the following books:\n\n"
    for book in books:
        try:
            title, author = book.split(" by ")
            prompt += f"- {title} by {author}\n"
        except ValueError:
            return "Please enter books in the format 'Title by Author'."

    prompt += (
    "\nBased on this list, recommend 5 books I’ll love 🧡. Keep responses SHORT (3-4 lines per book), include emojis 🎯📚✨, and skip long analysis.\n"
    "For each book, give:\n"
    "1. A quick blurb or vibe 🎭\n"
    "2. Why it matches my taste 🧠\n"
    "3. A similar book I’ve read 📖\n"
    "Make it warm, fun, and human — like a friend texting recs 💬💡"
    )

    return query_huggingface(prompt)

# Command-line usage
if __name__ == "__main__":
    print("📚 Book Recommender AI (Free Edition using Hugging Face)")
    print("Enter your favorite books (e.g. 'Hamnet by Maggie O'Farrell'). Enter 'done' when finished.")
    
    books_input = ""
    while True:
        book = input("Enter a book: ")
        if book.strip().lower() == "done":
            break
        books_input += book + "\n"

    print("\n⏳ Generating personalized recommendations...\n")
    recommendations = get_recommendations(books_input)
    print(recommendations)
