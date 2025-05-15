**Note**: You can install these using `pip install -r requirements.txt`.  
The `torch` package is needed for `transformers`, and `tk` is required for the GUI. If `tk` gives issues via pip (common on some Linux distros), you may need to install it via system package manager (like `sudo pacman -S tk` on Arch).

---

# Saree Assistant

A simple and elegant desktop assistant that answers your questions about traditional Indian sarees like Banarasi, Kanjeevaram, Bandhani, and more using Wikipedia-sourced data and a lightweight NLP model (`distilbert-base-uncased`).

---

## 🧠 What It Does

- **Web Scraper**: Pulls introductory paragraphs from Wikipedia pages of various sarees.
- **NLP QA System**: Uses Hugging Face's DistilBERT model to answer questions about sarees based on the scraped data.
- **GUI**: Built with Tkinter to create an intuitive desktop interface.
- **Saves Data**: Extracted content is saved as `sarees.json` and used as the model's context.

---

## 📂 Project Structure

### 🔹 Core Submission Package

```text
saree-assistant/
│
├── scraper.py         # Scrapes Wikipedia pages and creates sarees.json
├── query.py           # Loads QA pipeline and handles queries
├── tk_gui.py          # GUI interface using Tkinter
├── sarees.json        # Auto-generated context file for the model
├── requirements.txt   # List of Python package dependencies
├── README.md          # Project documentation and setup guide
```

This is the **minimal, essential version of the project**, included in the **Google Drive submission**. It contains all the necessary components to run and test the saree assistant without additional setup clutter.

---

### 🔸 Full Local Development Folder

```text
├── data
│   └── sarees.json             # Stored scraped saree info (same as in root)
├── env                         # Python virtual environment
│   ├── bin, lib, include...    # Environment-specific binaries and packages
├── folder_structure.txt        # Output of `tree` command
├── main.py                     # Alternate integration or testing script
├── models                      # Placeholder or model-related assets
├── __pycache__                 # Python bytecode cache
│   └── query.cpython-313.pyc
├── query.py                    # Handles natural language queries
├── README.md                   # This documentation
├── requirements.txt            # Python dependencies
├── saree_data_simple.json      # Simplified or partial saree dataset
├── sarees.json                 # Full scraped data
├── scraper.py                  # Wikipedia scraping script
├── src
│   └── Untitled.jpg            # Optional/test image
├── streamlit_app.py            # Alternative Streamlit-based interface
├── structured_sarees.json      # Variant with formatted data
└── tk_gui.py                   # Main Tkinter GUI interface
```

This is your **complete local development snapshot**, which includes virtual environments, test scripts, and alternate data/UX interfaces. It **won’t be part of the final submission**, but is documented here for clarity.

---

## 📦 Installation & Setup

You can run this project on your system using Python (recommended 3.8+). Follow these steps:

### Step 1: Clone the Project

 git clone https://github.com/mas622424/Under-Graduate-Project.git
 cd Under-Graduate-Project/saree-assistant


```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:

- `requests` and `beautifulsoup4` for scraping
- `transformers` from Hugging Face for the QA model
- `Pillow` for GUI image rendering
- `tkinter` (comes built-in with Python)
- `torch` for the backend of `transformers`

---

## 🚀 How to Run

### 1. Scrape Wikipedia and Generate Data

```bash
python scraper.py
```

This will create a `sarees.json` file with relevant content for answering queries.

### 2. Run the GUI Application

```bash
python tk_gui.py
```

You’ll see a beautiful interface where you can type questions like:

> "What is special about Banarasi sarees?"

Or use quick buttons like "Banarasi", "Kanjeevaram", etc.

---

## 🔍 About the Model

This project uses:

> **`distilbert-base-uncased`** – a smaller, faster alternative to BERT that retains 97% of its language understanding while being 60% faster.

**Why this model?**
- Lightweight: Perfect for a desktop assistant.
- No fine-tuning needed.
- Excellent general question-answering performance.

---

## 💡 Notes

- If you don’t have `orb.png`, the app defaults to a star emoji 🌟 as an icon.
- You may find **commented code** and **alternate interfaces** in earlier versions (`main.py`, etc.). These were part of the development process and can be safely ignored.
- You can expand the saree list in `scraper.py` by adding more URLs from Wikipedia.

---

## ✅  Notes


- Do **not** forget to run `scraper.py` at least once before trying the GUI — otherwise, `sarees.json` won’t exist.


## 👤 Author

Ajay Sankar Makkena-210077
Professor Tushar Sandhan-IIT Kanpur-Guide
