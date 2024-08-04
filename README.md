# Entity Extraction Comparison

This repository contains a Python script to extract named entities (e.g., persons, organizations, locations) from a contemporary news article using two approaches: SpaCy for a machine learning-based method and NLTK for a rule-based method. The script fetches news articles using the News API and compares the results of entity extraction between the two approaches.

## Requirements

- Python 3.6 or higher
- SpaCy
- NLTK
- Requests

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/entity-extraction-comparison.git
    cd entity-extraction-comparison
    ```

2. Install the required Python libraries:
    ```bash
    pip install spacy
    pip install nltk
    pip install requests
    ```

3. Download the SpaCy English model:
    ```bash
    python -m spacy download en_core_web_sm
    ```

## Usage

1. Replace `'YOUR_ACTUAL_NEWS_API_KEY'` with your actual News API key in the `entity_extraction_comparison.py` script.
2. Run the script:
    ```bash
    python entity_extraction_comparison.py
    ```

## Explanation

The script performs the following steps:

1. Fetches the top headlines from the News API.
2. Extracts the title and description of the first article.
3. Uses SpaCy to extract named entities from the article content.
4. Uses NLTK to extract named entities from the same article content.
5. Compares the entities extracted by SpaCy and NLTK and prints the differences.

### Example Output

