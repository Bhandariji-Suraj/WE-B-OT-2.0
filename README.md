Website Navigation Bot using BM25
Features
✅ Natural language query input
✅ BM25-based semantic ranking
✅ Clean and minimal web interface
✅ Flask backend with REST API
✅ Live score display of relevance
Project Structure

project/
│
├── backend/
│   ├── app.py              # Flask server
│   ├── bm25_model.py       # BM25 search model
│   ├── data_loader.py      # Loads the CSV data
│   └── data/
│       └── summary_df.csv  # Dataset with summaries and links
│
├── frontend/
│   ├── index.html          # UI markup
│   ├── app.js              # Fetch logic & DOM manipulation
│   └── style.css           # Styling
│
├── requirements.txt        # Python dependencies
└── README.md               # Project overview (this file)

Dataset
- summary_df.csv:
  - Summary: Text description of content
  - Link: Corresponding webpage link
Installation

Backend (Python + Flask)
1. Clone the repo
   git clone https://github.com/your-username/navigation-bot-bm25.git
   cd navigation-bot-bm25

2. Create a virtual environment
   python -m venv venv
   source venv/bin/activate  # on Windows: venv\Scripts\activate

3. Install dependencies
   pip install -r requirements.txt

4. Run the Flask app
   python backend/app.py

Frontend (HTML + JS)
1. Make sure index.html, app.js, and style.css are placed in the frontend/ folder.
2. Open http://127.0.0.1:5000 in your browser to use the bot.

Example Usage
Enter a query like:
"find tutorials on Python basics"
The system will return a list of relevant links ranked by relevance score.
Technologies Used
- Python, Flask – Backend and API
- BM25 (rank_bm25) – Search ranking algorithm
- nltk – Tokenization
- HTML/CSS/JavaScript – Frontend UI
To-Do / Enhancements
- Add support for advanced NLP (e.g., BERT or TF-IDF as fallback)
- Enable pagination of search results
- Integrate user feedback loop to improve ranking
Contributing
Pull requests are welcome! If you have any ideas to improve this bot, feel free to fork and contribute.
License
This project is open-source and available under the MIT License.
Author
Created by Your Name
GitHub: https://github.com/your-username
