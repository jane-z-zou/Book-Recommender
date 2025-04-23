import json
from openai import OpenAI
from config import OPENAI_API_KEY

# Initialize OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

# Load your books from a JSON file
def load_books(filepath="books.json"):
    with open(filepath, "r") as f:
        return json.load(f)

# Generate recommendations using the refined prompt
def get_recommendations(book_list):
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

    # Make API call
    response = client.chat.completions.create(
        model="gpt-4o",  # or "gpt-4" or "gpt-3.5-turbo"
        messages=[
            {"role": "system", "content": "You are a literary assistant who gives deeply personalized book recommendations."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.8
    )

    return response.choices[0].message.content

# Main function
def main():
    books = load_books()
    recommendations = get_recommendations(books)
    print("\n📚 Personalized Book Recommendations:\n")
    print(recommendations)

if __name__ == "__main__":
    main()