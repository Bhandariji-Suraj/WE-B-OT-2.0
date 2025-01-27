from flask import Flask, request, jsonify, send_from_directory
from data_loader import load_data
from bm25_model import BM25Model
import os

app = Flask(__name__, static_folder='../frontend', static_url_path='')

# Load data and initialize BM25
data = load_data("data/summary_df.csv")
bm25_model = BM25Model(data['Summary'], data['Link'])

@app.route('/')
def home():
    # Serve the frontend HTML
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.json.get('query', '')
    if not query:
        return jsonify({'error': 'Query is required'}), 400
    results = bm25_model.search(query)
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
