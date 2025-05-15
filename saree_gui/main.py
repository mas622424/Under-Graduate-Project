#tk_gui.py
import tkinter as tk
from query import answer_query

def get_answer():
    question = entry.get()
    answer = answer_query(question)
    result_label.config(text=answer)

# Create GUI window
root = tk.Tk()
root.title("Saree Query Assistant")

# Input field
entry = tk.Entry(root, width=50)
entry.pack(pady=10)

# Submit button
button = tk.Button(root, text="Ask", command=get_answer)
button.pack()

# Result label
result_label = tk.Label(root, text="", wraplength=400, justify="left")
result_label.pack(pady=10)

root.mainloop()

#query.py
import transformers
from transformers import pipeline
import json

# Load the small language model (QA pipeline)
qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased")

# Load saree data
with open("sarees.json", "r") as f:
    saree_data = json.load(f)

def answer_query(question):
    # Identify which saree is mentioned in the question
    for saree, context in saree_data.items():
        if saree.lower() in question.lower():
            result = qa_pipeline(question=question, context=context)
            return result["answer"]
    
    return "I don't have information on that."

if __name__ == "__main__":
    print(answer_query("What is special about Banarasi sarees?"))

    
#scraper.py
import requests
from bs4 import BeautifulSoup
import json

sarees = {
    "Banarasi": "https://en.wikipedia.org/wiki/Banarasi_sari",
    "Kanjeevaram": "https://en.wikipedia.org/wiki/Kanchipuram_sari",
    "Chanderi": "https://en.wikipedia.org/wiki/Chanderi_saree",
    "Bandhani": "https://en.wikipedia.org/wiki/Bandhani",
    "Sambalpuri": "https://en.wikipedia.org/wiki/Sambalpuri_saree"
}

def scrape_saree_info():
    saree_data = {}

    for name, url in sarees.items():
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract first 3 non-empty paragraphs for better context
        paragraphs = soup.find_all("p")
        text = " ".join([p.text.strip() for p in paragraphs if p.text.strip()][:3])

        saree_data[name] = text if text else "No data available"

    # Save as JSON
    with open("sarees.json", "w", encoding="utf-8") as f:
        json.dump(saree_data, f, indent=4, ensure_ascii=False)

    return saree_data

if __name__ == "__main__":
    saree_data = scrape_saree_info()
    print("Scraped data saved to sarees.json")

#query.py
from transformers import pipeline
import json

# ✅ Load the fine-tuned QA model (trained on SQuAD)
qa_pipeline = pipeline(
    "question-answering",
    model="distilbert-base-uncased-distilled-squad",
    tokenizer="distilbert-base-uncased-distilled-squad"
)

# Load saree data
with open("sarees.json", "r") as f:
    saree_data = json.load(f)

def answer_query(question):
    matched_contexts = []

    # Identify which sarees are mentioned in the question
    for saree, context in saree_data.items():
        if saree.lower() in question.lower():
            matched_contexts.append((saree, context))

    if matched_contexts:
        answers = []
        for saree, context in matched_contexts:
            try:
                result = qa_pipeline(question=question, context=context)
                answers.append(f"{saree}: {result['answer']}")
            except Exception as e:
                answers.append(f"{saree}: Sorry, couldn't process.")

        return "\n".join(answers)

    return "I don't have information on that. Please ask about a specific saree like Banarasi, Kanjeevaram, etc."

if __name__ == "__main__":
    query = "What is special about Banarasi and Kanjeevaram sarees?"
    print(answer_query(query))


#another gui
import tkinter as tk
from tkinter import scrolledtext
from query import answer_query

# Colors
bg_color = "#e6f2e6"     # light greenish white
primary_color = "#2e8b57"  # sea green
text_color = "#1c1c1c"

# Create the main application window
root = tk.Tk()
root.title("Saree Assistant")
root.geometry("650x450")
root.configure(bg=bg_color)

# Label
label = tk.Label(root, text="🌸 Ask about a saree:", font=("Helvetica", 16, "bold"),
                 bg=bg_color, fg=primary_color)
label.pack(pady=(20, 10))

# Text input for question
entry_frame = tk.Frame(root, bg=bg_color)
entry_frame.pack()
entry = tk.Entry(entry_frame, width=60, font=("Helvetica", 13), bd=2, relief="solid",
                 highlightthickness=1, highlightbackground=primary_color, highlightcolor=primary_color)
entry.pack(pady=5)

# Function to run when button is clicked
def get_answer():
    question = entry.get()
    output_box.delete("1.0", tk.END)
    if not question.strip():
        output_box.insert(tk.END, "⚠️ Please enter a question.")
        return
    answer = answer_query(question)
    output_box.insert(tk.END, answer)

# Button
ask_button = tk.Button(root, text="Get Answer", command=get_answer,
                       font=("Helvetica", 12, "bold"),
                       bg=primary_color, fg="white", padx=10, pady=5,
                       activebackground="#3cb371", relief="flat", cursor="hand2")
ask_button.pack(pady=10)

# Output box
output_box = scrolledtext.ScrolledText(root, height=12, width=70, font=("Helvetica", 12),
                                       bd=2, relief="solid", highlightthickness=1,
                                       highlightbackground=primary_color, highlightcolor=primary_color,
                                       wrap="word")
output_box.pack(pady=(5, 20))

# Run the GUI event loop
root.mainloop()


#scraping using re
import requests
from bs4 import BeautifulSoup
import json
import re

HEADERS = {"User-Agent": "Mozilla/5.0"}

SAREES = {
    "Banarasi": {
        "wiki": "https://en.wikipedia.org/wiki/Banarasi_sari"
    },
    "Chanderi": {
        "wiki": "https://en.wikipedia.org/wiki/Chanderi_sari"
    }
}

# Materials, features, occasions keywords to search
MATERIALS = ["silk", "cotton", "zari", "brocade", "chiffon", "georgette", "organza"]
FEATURES = ["weaving", "motif", "pattern", "design", "border", "pallu", "embroidery", "zari", "gold", "silver"]
OCCASIONS = ["wedding", "festival", "festive", "ceremony", "celebration"]
TIME_PATTERNS = r"\b(?:\d{1,2}\s*(?:days?|weeks?|months?))\b"

def get_text_from_url(url):
    try:
        res = requests.get(url, headers=HEADERS)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "lxml")
        paragraphs = soup.find_all("p")
        return " ".join(p.get_text(strip=True) for p in paragraphs)
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return ""

def extract_simple(text):
    result = {
        "Region": None,
        "Material": "",
        "Features": [],
        "TimeToMake": None,
        "CulturalSignificance": None,
        "Occasions": [],
    }

    # Try to detect region from known state/city keywords
    locations = ["Varanasi", "Uttar Pradesh", "Chanderi", "Madhya Pradesh", "India"]
    for loc in locations:
        if loc.lower() in text.lower():
            result["Region"] = loc
            break

    result["Material"] = ", ".join(sorted(set([mat for mat in MATERIALS if mat in text.lower()])))
    result["Features"] = sorted(set([feat for feat in FEATURES if feat in text.lower()]))

    match = re.search(TIME_PATTERNS, text.lower())
    if match:
        result["TimeToMake"] = match.group()

    detected_occasions = [occ.title() for occ in OCCASIONS if occ in text.lower()]
    result["Occasions"] = detected_occasions
    if detected_occasions:
        result["CulturalSignificance"] = "Worn during " + " and ".join(detected_occasions).lower()

    return result

def scrape_simple():
    output = {}
    for name, urls in SAREES.items():
        print(f"🔍 Scraping {name} Wikipedia page...")
        wiki_url = urls.get("wiki")
        if not wiki_url:
            continue

        text = get_text_from_url(wiki_url)
        info = extract_simple(text)

        output[name] = {
            **info,
            "Description": text[:1500] + "...",
            "Sources": [wiki_url]
        }

    with open("saree_data_simple.json", "w", encoding="utf-8") as f:
        json.dump(output, f, indent=4, ensure_ascii=False)

    print("✅ Data saved to 'saree_data_simple.json'")

if __name__ == "__main__":
    scrape_simple()


#another query.py
from transformers import pipeline
import json

# ✅ Load the QA pipeline using DistilBERT fine-tuned on SQuAD
qa_pipeline = pipeline(
    "question-answering",
    model="distilbert-base-uncased-distilled-squad",
    tokenizer="distilbert-base-uncased-distilled-squad"
)

# ✅ Load saree data
with open("/home/tron/saree_query_app/sarees.json", "r") as f:
    saree_data = json.load(f)

def answer_query(question):
    matched_contexts = []

    # Match sarees in the question
    for saree, context in saree_data.items():
        if saree.lower() in question.lower():
            matched_contexts.append((saree, context))

    if matched_contexts:
        answers = []
        for saree, context in matched_contexts:
            try:
                # Use only the 'Description' text as context
                result = qa_pipeline(
                    question=question,
                    context=context["Description"]
                )
                answers.append(f"{saree}: {result['answer']}")
            except Exception as e:
                answers.append(f"{saree}: Sorry, couldn't process. ({e})")

        return "\n".join(answers)

    return "I don't have information on that. Please ask about a specific saree like Banarasi, Chanderi, etc."

# ✅ Example usage
if __name__ == "__main__":
    query = "What is special about Banarasi and Chanderi sarees?"
    print(answer_query(query))
