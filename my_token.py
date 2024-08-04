import requests
import spacy
import nltk
from nltk import word_tokenize, pos_tag, ne_chunk

API_KEY = '239a21ae31b8477592d0f836c4c1fd43'
URL = 'https://newsapi.org/v2/top-headlines'
PARAMS = {
    'country': 'us',
    'apiKey': API_KEY
}

# Fetch a news article
response = requests.get(URL, params=PARAMS)
data = response.json()

# Check if the response contains the 'articles' key
if 'articles' not in data or len(data['articles']) == 0:
    print("No articles found or 'articles' key missing in the response. Response data:")
    print(data)
else:
    # Ensure title and description are not None
    article_title = data['articles'][0].get('title', 'No title available')
    article_description = data['articles'][0].get('description', 'No description available')
    
    # Handle cases where title or description might be None
    if article_title is None:
        article_title = 'No title available'
    if article_description is None:
        article_description = 'No description available'
    
    article_content = article_title + '. ' + article_description
    print("News Article Content:\n", article_content)

    # Extract named entities using SpaCy
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(article_content)
    spacy_entities = [(ent.text, ent.label_) for ent in doc.ents]
    print("\nNamed Entities using SpaCy:")
    for entity in spacy_entities:
        print(entity)

    # Download NLTK data files (if not already downloaded)
    try:
        nltk.download('punkt')
        nltk.download('maxent_ne_chunker')
        nltk.download('words')
        nltk.download('averaged_perceptron_tagger')
    except Exception as e:
        print("Error downloading NLTK resources:", e)

    # Extract named entities using NLTK
    tokens = word_tokenize(article_content)
    tags = pos_tag(tokens)
    try:
        nltk_entities = ne_chunk(tags)
        nltk_named_entities = []
        for chunk in nltk_entities:
            if hasattr(chunk, 'label'):
                entity = ' '.join(c[0] for c in chunk)
                label = chunk.label()
                nltk_named_entities.append((entity, label))
        print("\nNamed Entities using NLTK:")
        for entity in nltk_named_entities:
            print(entity)
    except LookupError as e:
        print("LookupError:", e)

    # Function to compare and display results
    def compare_entities(spacy_entities, nltk_entities):
        spacy_set = set(spacy_entities)
        nltk_set = set(nltk_entities)

        print("\nComparison of Named Entities:")
        print("\nEntities found by SpaCy but not by NLTK:")
        for entity in spacy_set - nltk_set:
            print(entity)

        print("\nEntities found by NLTK but not by SpaCy:")
        for entity in nltk_set - spacy_set:
            print(entity)

    # Compare and display results
    compare_entities(spacy_entities, nltk_named_entities)
